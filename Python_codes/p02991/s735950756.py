import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(3*N)]
for _ in range(M):
  u, v = map(lambda x:int(x)-1, input().split())
  graph[3*u+0] += [[3*v+1, 1]]
  graph[3*u+1] += [[3*v+2, 1]]
  graph[3*u+2] += [[3*v+0, 1]]

def dijkstra(s):
  dist = [float('inf')]*(3*N)
  dist[s] = 0
  num = [0]*(3*N)
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

S, T = map(lambda x:int(x)-1, input().split())
dist, _ = dijkstra(3*S)

if dist[3*T] == float('inf'):
  print(-1)
else:
  print(dist[3*T]//3)