N, M = map(int, input().split())
to = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    to[a].append(b)

S, T = map(int, input().split())

from collections import deque

q = deque([(S, 0)])
v = [[-1] * 3 for i in range(N+1)]

while q:
    a, t = q.popleft()
    b = t % 3
    if v[a][b] != -1:
        continue
    v[a][b] = t
    t += 1
    for x in to[a]:
        q.append((x, t))
    #print(q)


if v[T][0] == -1:
    print("-1")
else:
    print(v[T][0] // 3)