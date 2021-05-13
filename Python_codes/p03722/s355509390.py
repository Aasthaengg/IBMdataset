n, m = map(int, input().split())
std = []
for _ in range(m):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  std += [[a, b, -c]]

def bellman_ford(s):
  # std = [[s0, t0, d0], [s1, t1, d1], ... , [sm, tm, dm]]
  # (si, ti, di): si, ti間に重さdiの辺がある
  dist = [float('inf')]*n 
  dist[s] = 0
  for u in range(n):
    for s, t, d in std:
      if dist[t] > dist[s] + d:
        dist[t] = dist[s] + d
        if u == n-1 and t == n-1:
          return -1
  return dist

dist = bellman_ford(0)
if dist != -1:
  print(-dist[n-1])
else:
  print('inf')