import sys
from heapq import heappush, heappop
from collections import Counter


N, K = map(int, input().split())
#sushi = [list(map(int, x.split())) for x in sys.stdin.readlines()]
sushi = [list(map(int, input().split())) for _ in range(N)]

sushi.sort(key=lambda x: x[1], reverse=True)

base = 0
ate = Counter()
q = []
for i in range(K):
    t, d = sushi[i]
    base += d
    heappush(q, (d, t))
    ate[t] += 1

var = len(list(ate.keys()))
candidate = [base + var ** 2]
for i in range(K, N):
    t, d = sushi[i]
    if ate[t] == 0:
        while len(q):
            dx, tx = heappop(q)
            if ate[tx] > 1:
                break
        else:
            break
        ate[t] += 1
        ate[tx] -= 1
        base += d - dx
        var += 1
        candidate.append(base + var ** 2)

print(max(candidate))
