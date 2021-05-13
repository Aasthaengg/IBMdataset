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
inf = float("inf")

n,m = I()
a =[l() for _ in range(n)]

a.sort()
i = 0
while m != 0:
    if a[i][1] >= m :
        ans += m*a[i][0]
        break
    else:
        ans += a[i][0]*a[i][1]
        m -= a[i][1]
        i += 1

print(ans)
