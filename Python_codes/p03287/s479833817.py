import itertools
from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

A[0] %= M
ct = Counter(itertools.accumulate(A, lambda x, y: (x + y) % M))
ans = ct[0]
for value in ct.values():
    ans += (value * (value - 1)) // 2
print(ans)
