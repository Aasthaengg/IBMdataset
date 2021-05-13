import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

import math

n, h = na()
a = []
b = []
for i in range(n):
    _a, _b = na()
    a.append(_a)
    b.append(_b)

a.sort(reverse=True)
b.sort(reverse=True)

i = 0
cnt = 0
while h > 0:
    if i < n and a[0] < b[i]:
        h -= b[i]
        i += 1
        cnt += 1
    else:
        cnt += math.ceil(h / a[0])
        break

print(cnt)