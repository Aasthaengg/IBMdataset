t,r,g=map(int,input().split())
d=[[float("INF") for ccc in range(t)] for i in range(t)]
for i in range(t):
    d[i][i]=0
gl=list(map(int,input().split()))
for j in range(r):
    x,y,c=map(int,input().split())
    d[x-1][y-1]=c
    d[y-1][x-1]=c
for i in range(t):
    for j in range(t):
        for k in range(t):
            d[k][j]=min(d[k][j],d[k][i]+d[i][j])
from itertools import permutations as pe
ans=float("INF")
for G in pe(gl):
    p=0
    for qw in range(g-1):
        p+=d[G[qw]-1][G[qw+1]-1]
    ans=min(ans,p)
print(ans)