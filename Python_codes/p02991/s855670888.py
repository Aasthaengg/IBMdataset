from collections import deque

n, m = map(int, input().split())
F = [set() for _ in range(3*n)]
for _ in range(m):
  u, v = map(int, input().split())
  u = (u-1)*3
  v = (v-1)*3
  F[u].add(v+1)
  F[u+1].add(v+2)
  F[u+2].add(v)
s, t = map(int, input().split())
s = (s-1)*3
t = (t-1)*3
dist = [-1]*(3*n)
dist[s] = 0
dq = deque([s])
while dq:
  v = dq.popleft()
  for nv in F[v]:
    if dist[nv] != -1:
      continue
    dist[nv] = dist[v]+1
    dq.append(nv)
    if nv == t:
      break
  else:
    continue
  break
print(dist[t]//3)