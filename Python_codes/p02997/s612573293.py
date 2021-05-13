import sys
from itertools import combinations

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
limit = (N-1) * (N-2) // 2
if K > limit:
    print(-1); exit()

A = [(1, x) for x in range(2, N+1)]
# limit - K だけ辺を引く
for i, (x, y) in zip(range(limit-K), combinations(range(2, N+1), 2)):
    A.append((x, y))

print(len(A))
for a in A:
    print(*a)
