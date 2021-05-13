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

n = ni()
s = ns()

b, w = 0, 0
cub = [0] * (n + 1)
cuw = [0] * (n + 1)
for i in range(1, n + 1):
    cub[i] = cub[i - 1]
    cuw[i] = cuw[i - 1]
    cub[i] += s[i - 1] == '#'
    cuw[i] += s[i - 1] == '.'

ans = inf
for i in range(n + 1):
    ans = min(cub[i] + cuw[n] - cuw[i], ans)

print(ans)