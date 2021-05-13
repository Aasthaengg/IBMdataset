import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from math import gcd
N, K = mapint()
As = list(mapint())

if max(As)<K:
    print('IMPOSSIBLE')
else:
    g = 0
    for a in As:
        g = gcd(g, a)
    else:
        if K%g==0:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')