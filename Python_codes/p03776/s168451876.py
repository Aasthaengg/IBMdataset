from operator import mul
from functools import reduce

def nCr(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

n, a, b = (int(x) for x in input().split())
V = list(int(x) for x in input().split())
V.sort(reverse=True)

avg = sum(V[:a]) / a
k = V[:a].count(V[a - 1])
m = V.count(V[a - 1])
if k == a:
    ans = sum(nCr(m, i) for i in range(k, min(m, b) + 1))
else:
    ans = nCr(m, k)
print(avg)
print(ans)
