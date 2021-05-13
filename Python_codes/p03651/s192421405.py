# Author: cr4zjh0bp
# Created: Sun Mar 22 17:06:57 UTC 2020
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

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

g = a[0]
for i in range(n):
    g = gcd(g, a[i])

m = max(a)
if g == 1 and k <= m:
    print("POSSIBLE")
elif k % g == 0 and k <= m:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")