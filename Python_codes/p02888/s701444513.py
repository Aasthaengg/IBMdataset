import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")

n = k()
L = I()
p = sorted(L)
for i in range(n):
    for j in range(i+1,n):
        ans += bisect.bisect_left(p,p[i]+p[j])-(j+1)

print(ans)
