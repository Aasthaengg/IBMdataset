
import heapq
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(lambda x:int(x)-1, input().split())
  graph[a] += [[b,1]]
  graph[b] += [[a,1]]

def dijkstra(s):
  # numは最短経路の数
  dist = [float('inf')]*N
  dist[s] = 0
  num = [0]*N
  num[s] = 1
  q = [[0, s]]
  pre = [0]*N
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
        pre[v] = u
      elif dist[v] == dist[u] + weight:
        num[v] += num[u]
  return dist, num, pre

d1, _, pre1 = dijkstra(0)
d2, _, pre2 = dijkstra(N-1)

a1 = 0
a2 = 0
for i in range(N):
  if d1[i] <= d2[i]:
    a1 += 1
  else:
    a2 += 1

if a1 <= a2:
  print('Snuke')
else:
  print('Fennec')