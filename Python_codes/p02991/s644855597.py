from collections import deque
N,M = list(map(int, input().split()))

# node 3bai
# 0 N-1, N 2N-1, 2N 3N-1.
G = {}
for i in range(3*N):
  G[i] = []

for i in range(M):
  u,v = list(map(int, input().split()))
  u,v = u-1, v-1 # 0-indexed
  G[u].append(v+N)
  G[u+N].append(v+2*N)
  G[u+2*N].append(v)
  
S,T = list(map(int, input().split()))
S,T = S-1, T-1 # 0-indexed

q = deque()
visited = [False for i in range(3*N)]
willsearch = [False for i in range(3*N)]
dists = [-1 for i in range(3*N)]
q.append(S)
dists[S] = 0

while len(q) > 0:
  now = q.popleft()
  visited[now] = True
  for nextp in G[now]:
    if visited[nextp] or willsearch[nextp]:
      continue
    willsearch[nextp] = True
    q.append(nextp)
    dists[nextp] = dists[now] + 1
    
if dists[T] > 0:
  print(dists[T] // 3)
else:
  print(-1)