
from collections import defaultdict
from heapq import heappop, heappush

N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort(key=lambda x: x[1])
pq = []
f_x = 0
ctr = defaultdict(int)
appeared = 0
for _ in range(K):
    t, d = X.pop()
    heappush(pq, (d, t))
    appeared += int(ctr[t] == 0)
    f_x += d
    ctr[t] += 1

res = f_x + appeared ** 2
while pq or X:
    while pq:
        d, t = heappop(pq)
        if ctr[t] > 1:
            ctr[t] -= 1
            f_x -= d
            break

    if not pq:
        break

    while X:
        t_x, d_x = X.pop()
        if ctr[t_x] == 0:
            heappush(pq, (d_x, t_x))
            f_x += d_x
            ctr[t_x] += 1
            appeared += 1
            res = max(res, f_x + appeared ** 2)
            break

print(res)
