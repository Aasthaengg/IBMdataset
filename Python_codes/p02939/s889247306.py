# Author: cr4zjh0bp
# Created: Sun 15 Mar 2020 06:17:23 PM UTC
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

s = ns()
n = len(s)

p = ""
c = ""
ans = 0
i = 0
for i in range(n):
    c = c + s[i]
    if p != c:
        p = c
        c = ""
        ans += 1

print(ans)