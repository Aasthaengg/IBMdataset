import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7
import numpy as np

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
N = i()
S = [s() for _ in range(N)]
m = 0
a = 0
r = 0
c = 0
h = 0
for i in range(N):
    if S[i][0] == 'M':
        m += 1
    elif S[i][0] == 'A':
        a += 1
    elif S[i][0] == 'R':
        r += 1
    elif S[i][0] == 'C':
        c += 1
    elif S[i][0] == 'H':
        h += 1
cmbs = [m,a,r,c,h]
cmbs = itertools.combinations(cmbs,3)
ans = 0
for c in cmbs:
    ans += np.prod(list(c))
print(ans)