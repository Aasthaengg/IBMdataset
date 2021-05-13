def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


n,m,l= map(int,input().split()) #n:頂点数　w:辺の数

d=[[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    a,b,c = map(int,input().split())
    d[a-1][b-1]=c
    d[b-1][a-1]=c
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(d)

d2=[[float("inf") for i in range(n)] for i in range(n)] 
for i in range(n):
    for j in range(n):
        if d[i-1][j-1]<=l:
            d2[i-1][j-1]=1
            d2[j-1][i-1]=1
warshall_floyd(d2)
q=int(input())
l=[list(map(int, input().split())) for i in range(q)]
for i in range(q):
    if d2[l[i][0]-1][l[i][1]-1]-1!=float('inf'):
        print(d2[l[i][0]-1][l[i][1]-1]-1)
    else:
        print(-1)