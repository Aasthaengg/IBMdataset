import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    edge[x].append(y)
flag=[0]*n
dp=[0]*n
def dfs(s):
    if flag[s]:
        return dp[s]
    flag[s]=1
    dist=0
    for i in edge[s]:
        dist=max(dist,dfs(i)+1)
    dp[s]=dist
    return dp[s]
for i in range(n):
    dfs(i)
print(max(dp))