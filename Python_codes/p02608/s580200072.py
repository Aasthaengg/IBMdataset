import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random,resource

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
    n = I()

    a = [0] * n

    r = 0
    for x in range(1, 100):
        t = x ** 2
        if t > n:
            break

        for y in range(1, 100):
            u = t + y ** 2 + x * y
            if u > n:
                break

            for z in range(1, 100):
                v = u + z ** 2 + y * z + z * x
                if v > n:
                    break

                a[v-1] += 1

    return JA(a, "\n")


print(main())

