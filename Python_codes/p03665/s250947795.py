from collections import Counter
from functools import reduce
from operator import mul


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


N, P = list(map(int, input().split()))
A = Counter(list(map(lambda x: int(x) % 2, input().split())))
ans = 2 ** A[0]
if P:
    print(ans * sum(ncr(A[1], i) for i in range(1, A[1] + 1, 2)))
else:
    print(ans * sum(ncr(A[1], i) for i in range(0, A[1] + 1, 2)))
