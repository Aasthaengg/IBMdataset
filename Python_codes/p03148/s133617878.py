import sys
from itertools import accumulate
N, K = map(int, input().split())
dt = [tuple(map(int, sys.stdin.readline().split()))[::-1] for _ in range(N)]
dt.sort()
ans = sum([d for d, t in dt[N-K:]])
repet = []
seen = set()
for _ in range(K):
    d, t = dt.pop()
    if t not in seen:
        seen.add(t)
    else:
        repet.append(d)
sp = len(seen)
repet.append(0)
uniq = [0]
for _ in range(N-K):
    d, t = dt.pop()
    if t not in seen:
        uniq.append(d)
        seen.add(t)
repet = list(accumulate(repet[::-1]))
uniq = list(accumulate(uniq))
print(ans + max([(sp + i)**2 - r + u for i, (r, u) in enumerate(zip(repet, uniq))]))
