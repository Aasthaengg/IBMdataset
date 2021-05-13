import sys
from heapq import heappush, heappop


N, Q = map(int, input().split())
P = []
for i in range(1, N + 1):
    s, t, x = map(int, sys.stdin.readline().split())
    P.append((s - x, t - 1 - x, x))
P.sort()


q = []
cur = 0
ans = [-1] * Q
for i, d in enumerate(map(int, sys.stdin)):
    while cur < N and P[cur][0] <= d:
        s, t, x = P[cur]
        heappush(q, (x, t))
        cur += 1
    while q and q[0][1] < d:
        heappop(q)
    if q:
        ans[i] = q[0][0]

print(*ans, sep='\n')