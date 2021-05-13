import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x-1].append(y-1)
dp = [-1]*(n)
 
def dfs(i):
    if dp[i] != -1:
        return dp[i]
    else:
        res = 0
        for j in graph[i]:
            res = max(res,dfs(j)+1)
        dp[i] = res
        return dp[i]
 
for i in range(n):  
    dfs(i)
print(max(dp))