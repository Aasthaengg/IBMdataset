from collections import defaultdict
from operator import mul
from functools import reduce
def C(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

N = int(input())
d = defaultdict(int)
for _ in range(N):
    s = input()
    s = tuple(sorted(list(s)))
    d[s] += 1
ans = 0
for v in d.values():
    if v > 1:
        ans += C(v, 2)
print(ans)
