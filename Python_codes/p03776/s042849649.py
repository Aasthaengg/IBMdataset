from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N, A, B, *v = map(int, open(0).read().split())

v.sort(reverse=True)
answer = sum(v[:A]) / A
n = 0

if v[0] == v[A - 1]:
    N = v.count(v[0])
    n = cmb(N, min(N, B))
    tmp_cmb = n
    for i in range(min(B, N) - 1, A - 1, -1):
        tmp = N - i
        tmp_cmb = tmp_cmb * (i + 1) // tmp
        n += tmp_cmb
else:
    n = cmb(v.count(v[A - 1]), A - v.index(v[A - 1]))

print(answer)
print(n)