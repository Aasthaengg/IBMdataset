from collections import deque
N,M = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  adj[a].append(b)

S,T = map(int,input().split())
S -= 1
T -= 1

INF = float('inf')
dist = [ [INF]*3 for _ in range(N) ]
q = deque([(S,0)])
dist[S][0] = 0

while q:
  n,d = q.popleft()
  for v in adj[n]:
    nd = (d+1)%3
    if dist[v][nd] != INF: continue
    dist[v][nd] = dist[n][d]+1
    q.append((v,nd))

if dist[T][0] == INF:
  print(-1)
else:
  print(dist[T][0]//3)