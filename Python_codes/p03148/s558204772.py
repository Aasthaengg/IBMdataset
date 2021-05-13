import sys
input = sys.stdin.buffer.readline

n, k = map(int, input().split())
TD = [[0, 0] for _ in range(n)]
for i in range(n):
    t, d = map(int, input().split())
    TD[i][0], TD[i][1] = d, t

TD.sort(reverse=True)
S = set()
f = 0
h = []
import heapq
heapq.heapify(h)
for i in range(k):
    d, t = TD[i]
    if t in S:
        heapq.heappush(h, d)
    else:
        S.add(t)
    f += d

INF = 10**18
F = [-INF]*(k+1)
cur = len(S)
F[cur] = f

for i in range(k, n):
    d, t = TD[i]
    if t in S:
        continue
    else:
        if h:
            x = heapq.heappop(h)
            f += d-x
            S.add(t)
            cur += 1
            F[cur] = f

for i in range(0, k+1):
    F[i] += i*i

print(max(F))
