import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

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
    t = -1
    for i in range(1, 10**3):
        if i * (i+1) // 2 == n:
            t = i + 1
            break
    if t < 0:
        return 'No'
    a = [[] for _ in range(t)]
    k = 0
    for i in range(t):
        for j in range(i+1, t):
            k += 1
            a[i].append(k)
            a[j].append(k)
    r = ['Yes', str(len(a))]
    for c in a:
        r.append('{} {}'.format(len(c), ' '.join(map(str, c))))

    return '\n'.join(r)


print(main())
