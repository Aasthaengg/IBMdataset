import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

N, C, K =I()
T = []
for i in range(N):
    t = k()
    T.append(t)

T.sort()
a = T[0]+K
pas = 0
ans = 1

for i in range(N):
    if pas == C or a < T[i]:
        pas = 1
        ans += 1
        a = T[i]+K
    else:
        pas += 1

print(ans)
