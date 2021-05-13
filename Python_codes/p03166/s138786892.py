import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    G[x].append(y)

dp = [-1]*(n+1)
# dp[i]:頂点iに到達したときの有向辺の最長の長さ
def dfs(cur):
    if dp[cur] != -1:
        return dp[cur]
    res = 0
    for nx in G[cur]:
        res = max(res,dfs(nx)+1)
    dp[cur] = res
    return res
    
for i in range(n):
    dp[i] = max(dp[i],dfs(i))

print(max(dp))
