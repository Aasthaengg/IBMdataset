import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

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

n, k = na()
a = na()

ans = 0
for i in range(n):
    bl = 0
    al = 0
    for j in range(i):
        if a[j] < a[i]:
            bl += 1
    for j in range(i + 1, n):
        if a[j] < a[i]:
            al += 1
    
    ans += al * (k * (k + 1) // 2) + bl * (k * (k - 1) // 2)
    ans %= mod

print(ans % mod)