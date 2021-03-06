import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    a = [I() for _ in range(n)]
    if a[0] > 0:
        return -1
    for i in range(n-1):
        if a[i] < a[i+1] - 1:
            return -1
    r = a[-1]
    for i in range(n-2,-1,-1):
        if a[i] == a[i+1] - 1:
            continue
        r += a[i]

    return r




print(main())

