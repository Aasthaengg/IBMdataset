INF = float('inf')
def bellman_ford(n, edges, s):
  min_dist = [INF] * n

  min_dist[s] = 0

  for i in range(n):
    for (start, end, cost) in edges:
      if min_dist[start] != INF and min_dist[start] + cost < min_dist[end]:
        min_dist[end] = min_dist[start] + cost
        if i == n-1 and end == n-1:
          return -INF
  
  return min_dist

N, M = map(int, input().split())

edges = []

for i in range(M):
  edge = list(map(int, input().split()))
  edge[0] -= 1
  edge[1] -= 1
  edge[2] = -edge[2]
  edges.append(edge)
min_dist = bellman_ford(N, edges, 0)

if min_dist == -INF:
  print('inf')
else:
  print(-min_dist[-1])