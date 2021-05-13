import sys
input = sys.stdin.readline
N, M = map(int, input().split())
e = []
for _ in range(M):
  u, v, c = map(int, input().split())
  e.append((u, v, -c))
inf = 10 ** 18
d = [inf] * (N + 1)
d[1] = 0
for _ in range(N - 1):
  for u, v, c in e: d[v] = min(d[v], d[u] + c)
loop = []
for u, v, c in e:
  if d[v] > d[u] + c:
    d[v] = min(d[v], d[u] + c)
    loop.append(v)
if len(loop) == 0:
  print(-d[-1])
  exit(0)
for v in loop: d[v] = -inf
for _ in range(N - 1):
  for u, v, c in e:
    if v == N and (d[v] > d[u] + c): break
    d[v] = min(d[v], d[u] + c)
  else: continue
  break
else: 
  print(-d[-1])
  exit(0)
print("inf")