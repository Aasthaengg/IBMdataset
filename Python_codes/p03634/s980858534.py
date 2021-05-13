import sys
sys.setrecursionlimit(10**9)

N = int(input())
G = [[] for _ in range(N)]

for i in range(N-1):
  a, b, c = map(int, input().split())
  a, b = a-1, b-1
  G[a].append([b, c])
  G[b].append([a, c])

Q, K = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]

def dfs(v, pv=-1, d=0):
  dist[v] = d
  for nv, nd in G[v]:
    if nv == pv:
      continue
    dfs(nv, v, d+nd)

dist = [0]*N
dfs(K-1)

for x, y in query:
  x, y = x-1, y-1
  print(dist[x] + dist[y])