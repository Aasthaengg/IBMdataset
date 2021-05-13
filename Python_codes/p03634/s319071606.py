import heapq

N = int(input())

Tree = [[] for _ in range(N)]
for _ in range(N-1):
  a, b, c = map(int, input().split())
  Tree[a-1].append((c, b-1))
  Tree[b-1].append((c, a-1))

def dijkstra(s):
  hq = [(0, s)]
  heapq.heapify(hq)
  cost = [float('inf')] * N
  cost[s] = 0
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]:
      continue
    for d, u in Tree[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))
  return cost

Q, K = map(int, input().split())
cost = dijkstra(K-1)

for _ in range(Q):
  x, y = map(lambda x:int(x)-1, input().split())
  print(cost[x]+cost[y])