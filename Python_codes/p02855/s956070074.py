import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    h,w,k = LI()
    aa = [[c=="#" for c in S()] for _ in range(h)]
    rr = [[0]*w for _ in range(h)]
    t = 0
    for i in range(h):
        if not any(aa[i]):
            continue
        t += 1
        f = False
        for j in range(w):
            if aa[i][j]:
                if f:
                    t += 1
                else:
                    f = True
            rr[i][j] = t

        for ii in range(i+1,h):
            if any(aa[ii]):
                break
            for j in range(w):
                rr[ii][j] = rr[i][j]

        for ii in range(i-1,-1,-1):
            if any(aa[ii]):
                break
            for j in range(w):
                rr[ii][j] = rr[i][j]

    return JAA(rr,"\n", " ")


print(main())



