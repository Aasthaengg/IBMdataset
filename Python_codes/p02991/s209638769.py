from collections import defaultdict as dd
from collections import deque
N, M = map(int, input().split())
e = dd(list)
inf = 10 ** 9
for _ in range(M):
  u, v = map(int, input().split())
  e[u].append(v + N)
  e[u + N].append(v + 2 * N)
  e[u + 2 * N].append(v)
S, T = map(int, input().split())
S += 2 * N
T += 2 * N
stopped = [inf] * (3 * (N + 1))
Q = deque()
Q.append(S)
stopped[S] = 0
while len(Q) != 0:
  p = Q.popleft()
  if stopped[p] >= stopped[T]:
    break
  for q in e[p]:
    if stopped[q] > stopped[p] + 1:
      Q.append(q)
      stopped[q] = stopped[p] + 1
if stopped[T] == inf:
  print(-1)
else:
  print(stopped[T] // 3)