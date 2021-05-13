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
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

N,M = I()
C = [[] for _ in range(N+1)]
for i in range(M):
    p,y = I()
    C[p].append([y,i])
ans = ['a']*M
for i in range(1,len(C)):
    c = C[i]
    if c:
        c.sort()
        for j in range(len(c)):
            y,b = c[j]
            ans[b] = str(i).zfill(6)+str(j+1).zfill(6)
for a in ans:
    print(a)