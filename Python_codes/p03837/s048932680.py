from collections import defaultdict
from heapq import heappush, heappop
N, M = map(int, input().split())
dic = defaultdict(list)
Els = []
for i in range(M):
  a, b, c = map(int, input().split())
  dic[a-1] += [(b-1,c)]
  dic[b-1] += [(a-1, c)]
  Els += [(a-1,b-1,c)]

def dijkstra(s,e):
  dist = [float('inf')]*N
  dist[s] = 0
  q = [(0,s)]
  z = -1
  while q:
    c, v = heappop(q)
    if dist[v]<c:
      continue
    dist[v] = c
    for u, m in dic[v]:
      if dist[u]>dist[v]+m:
        dist[u] = dist[v]+m
        heappush(q,(dist[u],u))
        if u==e:
          z = v
  return z

ans = 0
for a, b, c in Els:
  if dijkstra(a,b)!=a:
    ans += 1
print(ans)