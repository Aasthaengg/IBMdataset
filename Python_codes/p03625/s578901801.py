# Author: cr4zjh0bp
# Created: Tue Mar 24 00:01:43 UTC 2020
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

from collections import Counter

n = ni()
a = na()
c = Counter(a)
m = list(c.items())
m.sort(reverse=True)
xy = [0] * 2
i = 0
flag = False
for k, v in m:
    if v >= 4:
        if i != 0:
            print(xy[0] * k)
        else:
            print(k * k)
        flag = True
        break
    elif v >= 2:
        xy[i] = k
        i += 1
        if i == 2:
            print(xy[0] * xy[1])
            flag = True
            break
if not flag:
    print(0)