import sys
sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
edge=[[] for _ in range(n)]
dp=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  edge[a-1].append(b-1)

def dfs(s):
  if edge[s]:
    for i in edge[s]:
      if dp[i]:dp[s]=max(dp[s],dp[i]+1)
      else:dp[s]=max(dp[s],dfs(i)+1)
    return dp[s]
  else:return 0
for i in range(n):
  dfs(i)
print(max(dp))