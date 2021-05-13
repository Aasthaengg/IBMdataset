
from collections import deque

N, M, P = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

to = [False] * (N + 1)
to[1] = True
q = deque([1])
while q:
    u = q.popleft()
    for a, b, c in X:
        if a == u and not to[b]:
            to[b] = True
            q.append(b)

ot = [False] * (N + 1)
ot[N] = True
q = deque([N])
while q:
    u = q.popleft()
    for a, b, c in X:
        if b == u and not ot[a]:
            ot[a] = True
            q.append(a)

INF = 10 ** 9 + 7
start = 1
d = [INF] * (N + 1)
d[start] = 0
updated = True
cnt = 0

while updated and cnt <= M:
    updated = False
    cnt += 1
    for u, v, c in X:
        if not to[u] or not ot[u] or not to[v] or not ot[v]:
            continue

        if d[v] > d[u] - (c - P):
            d[v] = d[u] - (c - P)
            updated = True

if cnt > N:
    print(-1)
else:
    print(max(0, -d[-1]))
