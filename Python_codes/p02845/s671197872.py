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
a = na()

x = 0
y = 0
z = 0

def count(m):
    cnt = 0
    cnt += x == m
    cnt += y == m
    cnt += z == m
    return cnt

ans = 1
for i in range(n):
    ans *= count(a[i])
    if x == a[i]:
        x += 1
    elif y == a[i]:
        y += 1
    elif z == a[i]:
        z += 1

print(ans % mod)