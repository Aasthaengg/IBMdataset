import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10**7)

ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

from collections import defaultdict

n = ni()
xy = nan(n)

dic = defaultdict(int)
for i in range(n):
    cx, cy = xy[i]
    cx += 10 ** 9
    cy += 10 ** 9
    for j in range(n):
        if i == j:
            continue
        nx, ny = xy[j]
        nx += 10 ** 9
        ny += 10 ** 9
        dic[(nx - cx, ny - cy)] += 1

m = 0
for k, v in dic.items():
    m = max(v, m)

ans = n - m
print(ans)