n,m,l=map(int,input().split())

#基本的にワーシャルフロイドの場合、行列式のリストで距離を保管する
from scipy.sparse import csr_matrix
from scipy.sparse import csgraph 
d = [[10**12 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    #有向グラフか無向グラフかによってここで場合わけが生じる
    d[x][y] = z
    d[y][x] = z
    
for i in range(n+1):
    d[i][i] = 0 #自身のところに行くコストは０
q=int(input())
que=[]
for _ in range(q):
    s,t=map(int,input().split())
    que.append((s,t))
       
csr=csr_matrix(d)
K=csgraph.shortest_path(csr,method="FW",directed=True)
e = [[10**12 for i in range(n+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if K[i][j]<=l:
            e[i][j]=1
            
for i in range(n+1):
    e[i][i]=0
    

A=csr_matrix(e)
ANS=csgraph.shortest_path(A,method="FW",directed=True)

for some in que:
    s,t=some[0],some[1]
    if int(ANS[s][t])<10**12:
        print(int(ANS[s][t])-1)
    else:
        print(-1)


