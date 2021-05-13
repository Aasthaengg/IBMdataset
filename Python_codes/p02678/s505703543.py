from heapq import heappop, heappush

INF = 1000000
N, M = map(int, input().split())
d = [INF]*(N+1)
d[1] = 0
prev = [0]*(N+1)
G = {}
for i in range(M):
  a, b = map(int, input().split())
  try:
    G[a].append(b)
  except:
    G[a] = [b]
  try:
    G[b].append(a)
  except:
    G[b] = [a]

que = []
heappush(que, (0, 1))
    
while True:
  if len(que) == 0:
    break
  p = heappop(que)
  v = p[1]
  
  for u in G[v]:
    if (d[u] > d[v] + 1):
      d[u] = d[v] + 1
      heappush(que, (d[u], u))
      prev[u] = v
      
if 0 in prev[2:]:print('No')
else:
  print('Yes')
  for i in range(2, N+1):
    print(prev[i])