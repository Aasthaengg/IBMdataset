def addEdge(adj, u, v):
    adj[u].append(v)
def dfs(node,dp,vis,adj):
    vis[node] = True 
    for i in range(len(adj[node])):
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], dp,vis,adj)
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())
adj = [[] for i in range(n + 1)] 
for i in range(m):
    u,v=map(int, input().split())
    addEdge(adj,u,v)
dp=[0]*(n+1)
vis=[False]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        dfs(i,dp,vis,adj)
ans=0
for i in range(1, n + 1):   
    ans = max(ans, dp[i])  
print(ans)
