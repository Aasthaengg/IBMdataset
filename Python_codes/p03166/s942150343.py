import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 1)

N,M = map(int,readline().split())

G = [[] for i in range(N)]

for i in range(M):
  x,y = map(int,readline().split())
  G[x - 1].append(y - 1)

dp = [-1] * N

def rec(v):
  if dp[v] != -1:
    return dp[v] # 更新済み
  
  res = 0
  for child in G[v]:
    res = max(res, rec(child) + 1)
    
  dp[v] = res
  return res

res = 0
for v in range(N):
  res = max(res, rec(v))
  
print(res)