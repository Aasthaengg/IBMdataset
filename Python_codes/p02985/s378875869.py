import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(lambda x:int(x)-1, input().split())
  graph[a] += [b]
  graph[b] += [a]

global ans
ans = K

def npr(n, r, p):
  e = 1
  for i in range(n, n-r, -1):
    e *= i
    e %= p

  return e
p=10**9+7

def dfs(u, pre):
  global ans
  child = 0
  for v in graph[u]:
    if v != pre:
      dfs(v, u)
      child += 1
  
  if u == 0:
    ans *= npr(K-1, child, p)
  else:
    ans *= npr(K-2, child, p)

  ans %= p

dfs(0, -1)
print(ans%p)
