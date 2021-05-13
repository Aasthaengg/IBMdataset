import sys
from heapq import heappush, heappop


I = sys.stdin.readlines()
N, Q = map(int, I[0].split())
P = []
for i in range(1, N + 1):
    s, t, x = map(int, I[i].split())
    P.append((s - x, t - 1 - x, x))
P.sort()
INF = float('inf')
P.append((INF, INF, INF))

q = []
cur = 0
s, t, x = P[cur]
for i in range(N + 1, N + Q + 1):
    d = int(I[i])
    while s <= d:
        heappush(q, (x, t))
        cur += 1
        s, t, x = P[cur]
    ans = -1
    while len(q) > 0:
        x1, t1 = q[0]
        if d <= t1:
            ans = x1
            break
        else:
            heappop(q)
    print(ans)

