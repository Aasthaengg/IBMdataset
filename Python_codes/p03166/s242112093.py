import sys
sys.setrecursionlimit(1000000)
def dfs(u):
    if(dp[u]!=-1):
        return dp[u]
    for i in d[u]:
        if(dp[i]!=-1):
            dp[u]=max(dp[u],dp[i]+1)
        else:
            dp[u]=max(dp[u],dfs(i)+1)
    return max(dp[u],0)
from collections import defaultdict as dd
n,m=map(int,input().split())
d=dd(list)
for i in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
dp=dd(lambda: -1)
mx=0
for i in range(1,n+1):
    if(dp[i]==-1):
        dp[i]=dfs(i)
    mx=max(mx,dp[i])
print(mx)