# Author: cr4zjh0bp
# Created: Fri Mar  6 03:39:35 UTC 2020
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

from collections import Counter

s = ns()
n = len(s)
k = ni()

l = []
for i in range(n):
    st = s[i]
    l.append(st)
    for j in range(1, min(k, n - i)):
        st += s[i + j]
        l.append(st)

c = Counter(l)
uni = list(c)
uni.sort()
print(uni[k - 1])