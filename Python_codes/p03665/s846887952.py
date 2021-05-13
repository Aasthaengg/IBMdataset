from collections import Counter
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(lambda x, y: x * y, range(n, n - r, -1), 1)
    denom = reduce(lambda x, y: x * y, range(1, r + 1), 1)
    return numer // denom


N, P = map(int, input().split())
A = Counter(map(lambda x: int(x) % 2, input().split()))
e = A.get(0, 0)
o = A.get(1, 0)
ans = 2 ** e
if P:
    if o == 0:
        print(0)
    else:
        ans *= sum(ncr(o, i) for i in range(1, o + 1) if i % 2)
        print(ans)
else:
    ans *= sum(ncr(o, i) for i in range(o + 1) if i % 2 == 0)
    print(ans)
