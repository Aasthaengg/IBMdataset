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
    pf(0)
    ta = ti = S()
    if ti == 'Vacant':
        return
    mi = 0
    ma = n
    while 1:
        mm = (mi+ma) // 2
        pf(mm)
        c = S()
        if c == 'Vacant':
            return
        if ti == c:
            if (mm - mi) % 2 == 0:
                mi = mm
                ti = c
            else:
                ma = mm
                ta = c
        else:
            if (mm - mi) % 2 == 1:
                mi = mm
                ti = c
            else:
                ma = mm
                ta = c

    return 'No'


main()


