import sys
import math
import numpy as np
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

N = i()
L = l()
c = Counter(L)
ans = 0
for i,v in c.items():
    if i > v:
        ans += v
    if i < v:
        ans += v-i
print(ans)