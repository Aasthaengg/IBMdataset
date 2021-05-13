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

sx, sy, tx, ty = na()

ans = []
for i in range(abs(sx - tx)):
    ans.append('R')

for i in range(abs(sy - ty)):
    ans.append('U')

ans.append('R')
for i in range(abs(sy - ty) + 1):
    ans.append('D')

for i in range(abs(sx - tx) + 1):
    ans.append('L')

ans.append('U')

for i in range(abs(sy - ty)):
    ans.append('U')

for i in range(abs(sx - tx)):
    ans.append('R')

ans.append('U')

for i in range(abs(sx - tx) + 1):
    ans.append('L')

for i in range(abs(sy - ty) + 1):
    ans.append('D')

ans.append('R')

print(*ans, sep="")