import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    if(dp[v]==-1):
        dp[v]=0
        for nv in G[v]:
            dp[v]=max(dp[v],dfs(nv)+1)
    return dp[v]
N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    G[x].append(y)
dp=[-1]*N
res=-1
for v in range(N):
    res=max(res,dfs(v))
print(res)