import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
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


def inv(x):
    return pow(x, mod - 2, mod)

cms = 10**5 + 5
cm = [0] * cms

def comb_init():
    cm[0] = 1
    for i in range(1, cms):
        cm[i] = cm[i-1] * i % mod

def comb(a, b):
    return (cm[a] * inv(cm[a-b]) % mod) * inv(cm[b]) % mod

def main():
    n,k = LI()
    ab = [LI_() for _ in range(n-1)]
    e = collections.defaultdict(list)
    for a,b in ab:
        e[a].append(b)
        e[b].append(a)

    for v in e.values():
        if len(v) >= k:
            return 0

    comb_init()
    def f(i, p):
        el = len(e[i])
        if p == -1:
            r = comb(k-1, el) * cm[el] % mod
        else:
            r = comb(k-2, el-1) * cm[el-1] % mod
        for c in e[i]:
            if c == p:
                continue
            r *= f(c, i)
            r %= mod
        return r

    r = f(0,-1) * k


    return r % mod


print(main())



