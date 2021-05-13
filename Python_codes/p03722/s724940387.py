import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N, M = map(int, input().split())
e = dd(list)
for _ in range(M):
  a, b, c = map(int, input().split())
  e[a].append((b, -c))
class BellmanFord:
  def __init__(self, n, e):
    self.n = n
    self.edges = []
    for k in e.keys():
      for t in e[k]:
        self.edges.append((k, t[0], t[1]))
  def path(self, s, t):
    d = [float("inf")] * (self.n + 1)
    d[s] = 0
    for i in range(self.n + 1):
      for (u, v, c) in self.edges:
        if d[u] != float("inf") and (d[u] + c < d[v]):
          d[v] = d[u] + c
          if i == self.n and (v == self.n):
            return "-loop"
    return d[t]
bf = BellmanFord(N, e)
res = bf.path(1, N)
if res == "-loop": print("inf")
else: print(-res)