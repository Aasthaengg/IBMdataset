from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
  x, y = map(lambda x: int(x)-1, input().split())
  graph[x].append(y)

dp = [-1]*N
def rec(v):
  if dp[v] != -1:
    return dp[v]
  
  res = 0
  for nv in graph[v]:
    res = max(res, rec(nv)+1)
  dp[v] = res
  return res

res = 0
for v in range(N):
  res = max(res, rec(v))
print(res)