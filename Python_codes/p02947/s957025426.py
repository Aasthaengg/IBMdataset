from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

from collections import Counter
n = int(input())
list_N = []
ans = 0

for _ in range(n):
    s = sorted(input())
    list_N.append("".join(s))

list_M = list(Counter(list_N).values())

for i in list_M:
    if i != 1:
        ans += cmb(i, 2)
print(ans)