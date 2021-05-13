from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N = int(input())

if N % 2:
    s = N
    print(cmb(N - 1, 2) - N // 2 + N - 1)
else:
    s = 1 + N
    print(cmb(N, 2) - N // 2)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        if i + j != s:
            print(i, j)