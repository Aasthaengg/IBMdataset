import heapq

H, W = map(int, input().split())
graph = []
wall = []

for _ in range(10):
  graph.append(list(map(int, input().split())))

for _ in range(H):
  wall += list(map(int, input().split()))

def dijkstra(s):
  INF = 10**5
  hq = [(0, s)]
  heapq.heapify(hq)
  cost = [INF] * 10
  cost[s] = 0
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue
    for u, d in enumerate(graph[v]):
      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))
  return cost[1]

mincost = [0]*10
for i in range(10):
  mincost[i] = dijkstra(i)

ans = 0
for x in wall:
  if x == -1 or x == 1:
    continue
  else:
    ans += mincost[x]

print(ans)