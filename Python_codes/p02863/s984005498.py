N, T = map(int, input().split())
A = []
for _ in range(N):
  a, b = map(int,input().split())
  A.append((a, b))
A.sort(key=lambda x: x[0])

newdp = [0 for _ in range(T)]
ans = 0
from collections import deque
A = deque(A)
visited = [0]
while A:
  olddp = tuple(newdp)
  newdp = list(newdp)
  X = A.popleft()
  a = X[0]
  b = X[1]
  for v in visited:
    if v + a > T-1:
      ans = max(ans, olddp[v]+b)
    else:

      if newdp[v+a] == 0:
        visited.append(v+a)
      newdp[v+a] = max(olddp[v] + b, newdp[v+a])


if ans == 0:
  print(max(olddp))
else:
  print(ans)