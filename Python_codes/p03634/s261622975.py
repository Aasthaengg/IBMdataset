import heapq
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  graph[a] += [[b, c]]
  graph[b] += [[a, c]]

Q, K = map(int, input().split())

def dijkstra(s):
  dist = [float('inf')]*N
  dist[s] = 0
  num = [0]*N
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

dist, _ = dijkstra(K-1)

for _ in range(Q):
  x, y = map(lambda x:int(x)-1, input().split())
  print(dist[x]+dist[y])