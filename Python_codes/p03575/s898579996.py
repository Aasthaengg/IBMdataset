import heapq
N, M = map(int, input().split())
ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
ans = 0

def dijkstra(s, graph, n):
  dist = [float('inf')]*n
  dist[s] = 0
  num = [0]*n
  num[s] = 1
  q = [[0, s]]
  heapq.heapify(q)
  while q:
    c, u = heapq.heappop(q)
    if dist[u] < c:
      continue
    for v, weight in graph[u]:
      if dist[v] > dist[u] + weight:
        dist[v] = dist[u] + weight
        num[v] = num[u]
        heapq.heappush(q, [dist[v], v])
      elif dist[v] == dist[u] + weight:
        num[v] += num[u]
  return dist, num

for i in range(M):
  graph = [[] for _ in range(N)]
  for j in range(M):
    if i != j:
      a, b = ab[j]
      graph[a] += [[b, 1]]
      graph[b] += [[a, 1]]

  for j in range(N):
    d, _ = dijkstra(j, graph, N)
    if max(d) == float('inf'):
      ans += 1
      break
print(ans)
