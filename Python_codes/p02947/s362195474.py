import bisect,collections,copy,heapq,itertools,math,string
from collections import defaultdict as D
from functools import reduce
import numpy as np
import sys
import os
from operator import mul
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353    

N = I()
s = [sorted(list(_S())) for _ in range(N)]
ss = [0] * N
for i in range(N):
    ss[i]=''.join(s[i])

c = collections.Counter(ss)

# nC2
def nCr(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

key, counts = zip(*c.most_common())
ans = 0
for  count in counts:
    if count > 1:
        ans += nCr(count,2)
print(ans)
# list(map(lambda n,r: nCr(n,r),counts))