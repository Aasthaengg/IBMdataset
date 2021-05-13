def BellmanFord(edges,num_v,source):
  inf=float("inf")
  dist=[inf for i in range(num_v)]
  dist[source-1]=0
  for i in range(num_v):
    for edge in edges:
      if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
        dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
        if i==num_v-1: dist[edge[1]-1] = -inf
  for i in range(num_v):
    for edge in edges:
      if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
        dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
  r = dist[-1]
  if r > 0: r = 0
  if r < 0: r=-r
  if r == inf: r=-1
  return r

import sys
input = sys.stdin.readline
N, M, P = map(int, input().split())
edges = []
for i in range(M):
    A, B, C = map(int, input().split())
    edges.append([A, B, P-C])
print(BellmanFord(edges, N, 1))
