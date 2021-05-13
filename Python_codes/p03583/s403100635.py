# Author: cr4zjh0bp
# Created: Sat Mar 14 14:07:54 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
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

N = ni()
m = 3500 // 4

def f():
    ans = []
    for h in range(3501):
        for n in range(3501):
            c = h * n * N
            d = 4 * h * n - N * n - N * h
            if d > 0 and c % d == 0:
                ans = [h, n, c // d]
                return ans

print(*f())