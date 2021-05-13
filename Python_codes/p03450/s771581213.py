import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
  l, r, d = map(int, input().split())
  l -= 1
  r -= 1
  G[l].append((r, d))
  G[r].append((l, -d))
dist = [float("inf")]*n
def dfs(v):
  for nv, d in G[v]:
    if dist[nv] == float("inf"):
      dist[nv] = dist[v]+d
      if not dfs(nv):
        return False
    else:
      if dist[nv] != dist[v]+d:
        return False
  return True
for i in range(n):
  if dist[i] == float("inf"):
    dist[i] = 0
    if not dfs(i):
      print("No")
      break
else:
  print("Yes")