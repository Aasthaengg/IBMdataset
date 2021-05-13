import sys
input = sys.stdin.readline
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
inf=float("inf")
n,m=map(int,input().split())
G=[[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    G[a-1][b-1]=c
    G[b-1][a-1]=c
#print(G)
from copy import deepcopy
H=deepcopy(G)
#print(H)
H=warshall_floyd(H)
#print(G,H)
cnt=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if G[i][j]==inf:
            continue
        if G[i][j]!=H[i][j]:
            cnt+=1
print(cnt//2)
