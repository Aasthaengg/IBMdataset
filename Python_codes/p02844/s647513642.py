from bisect import bisect_left, bisect_right
from itertools import product

n = int(input())
s = input()

A = [[] for _ in range(10)]
for i in range(n):
    x = int(s[i])
    A[x].append(i)

use = set((i for i in range(10) if len(A[i]) > 0))
ans = 0
for a, b, c in product(use, repeat=3):
    ai = A[a][0]
    ci = A[c][-1]
    k = bisect_right(A[b], ci - 1) - bisect_left(A[b], ai + 1)
    if k > 0:
        ans += 1
print(ans)
