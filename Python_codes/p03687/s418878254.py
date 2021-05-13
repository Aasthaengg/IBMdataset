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

from collections import Counter

s = ns()
c = Counter(s)

ans = inf
for i in c.keys():
    ns = i + s + i
    j = 1
    cur = 0
    res = 0
    while j < len(ns):
        if ns[j] == i:
            res = max(res, j - cur - 1)
            cur = j
        j += 1
    ans = min(ans, res)

print(ans)