import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    seen[v]=1
    for nv in G[v]:
        if seen[nv]:
            continue
        dfs(nv)
    topo.append(v)

N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    G[x].append(y)
seen=[0]*N
topo=[]
for i in range(N):
    if not seen[i]:
        dfs(i)
dp=[0]*N
for v in reversed(topo):
    for nv in G[v]:
        dp[nv]=max(dp[nv],dp[v]+1)
print(max(dp))