from itertools import permutations

def warshall_floyd(n, d):
    for k in range(n):
        for i in range(n): #始点
            for j in range(n): #終点
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

n,m,R=map(int,input().split())
r=list(map(int,list(input().split())))
g=[[float("inf")]*n for _ in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    g[a-1][b-1]=c
    g[b-1][a-1]=c
for i in range(n):
    g[i][i]=0
g=warshall_floyd(n,g)
ans=float("inf")
for p in list(permutations(r)):
    tmp=0
    for i in range(R-1):
        tmp+=g[p[i]-1][p[i+1]-1]
    ans=min(ans,tmp)
print(ans)
