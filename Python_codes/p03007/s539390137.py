import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
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
    a = sorted(LI())
    i = 0
    if a[0] >= 0:
        i = 0
    elif a[-1] <= 0:
        i = n - 2
    else:
        i = bisect.bisect_right(a,0) - 1

    r = []
    j = i + 1
    # print(a,i,j)
    for k in range(i-1,-1,-1):
        r.append('{} {}'.format(a[j], a[k]))
        a[j] -= a[k]
    for k in range(j+1,n):
        r.append('{} {}'.format(a[i], a[k]))
        a[i] -= a[k]
    r.append('{} {}'.format(a[j],a[i]))

    return '{}\n{}'.format(a[j]-a[i], JA(r, '\n'))


print(main())

