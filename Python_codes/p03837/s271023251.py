import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=10**9
w=[[INF]*n for i in range(n)]
for i in range(n):
    w[i][i]=0
V=[]
for i in range(m):
    a,b,c=map(int,input().split())
    V.append((a-1,b-1,c))
    w[a-1][b-1]=c
    w[b-1][a-1]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            w[i][j]=min(w[i][j],w[i][k]+w[k][j])
count=0
for v in V:
    short=False
    for i in range(n):
        for j in range(i+1,n):
            if w[i][j]==w[i][v[0]]+v[2]+w[v[1]][j] or w[i][j]==w[i][v[1]]+v[2]+w[v[0]][j]:
                short=True
    if not short:
        count+=1
print(count)

