#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

import sys
sys.setrecursionlimit(10**6)

def dfs(u):
    global grpah,vis,dp
    vis[u] = 1
    for i in graph[u]:
        if not vis[i]:
            dfs(i)
        dp[u] = max(dp[u],dp[i] + 1)

n,m = ip()
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = ip()
    graph[a].append(b)

dp = [0]*(n+1)
vis = [0]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        dfs(i)
#print(dp)
print(max(dp))