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

s = list(ns())
n = len(s)
k = ni()

for i in range(n):
    if s[i] != 'a':
        if ord('z') + 1 - ord(s[i]) <= k:
            k -= ord('z') + 1 - ord(s[i])
            s[i] = 'a'

if k >= 1:
    s[-1] = chr((ord(s[-1]) - ord('a') + k) % 26 + ord('a'))

print(*s, sep="")