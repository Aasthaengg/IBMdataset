import sys
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
  x,y=map(int,input().split())
  G[x-1].append(y-1)
  
dp = [-1]*N

def rec(v):
  if dp[v] != -1:
    return dp[v]
  res = 0
  for next_v in G[v]:
    res = max(res, rec(next_v)+1)
  dp[v] = res
  return dp[v]
  
for i in range(N):
  dp[i] = rec(i)
  
print(max(dp))