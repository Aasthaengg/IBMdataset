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

n = ni()

if n == 0:
    print(0)
else:
    ans = ""
    while n != 0:
        if n & 1:
            n -= 1
            ans = '1' + ans
        else:
            ans = '0' + ans
        n //= -2
    print(ans)