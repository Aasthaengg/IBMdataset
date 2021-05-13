from operator import mul
from functools import reduce
def comb2(n,r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

def examD():
    N, A, B = LI()
    v = LI(); v.sort(reverse = True)
    ans = sum(v[:A])/A
    d = defaultdict(int)
    for s in v:
        d[s] +=1
#    print(d)
    cur = A
    for i in v:
        if cur<=d[i]:
            break
        else:
            cur -=d[i]
    if i!=max(v):
        ansC = comb2(d[i],cur)
    else:
        ansC = 0
        for j in range(A,min(B,d[i])+1):
            ansC += comb2(d[i],j)
    print(ans)
    print(ansC)


import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
