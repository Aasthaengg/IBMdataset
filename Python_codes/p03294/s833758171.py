import sys
import math
import itertools
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

N = i()
a = l()
l = 1
for i in range(N):
    l *= a[i]
l -= 1
ans = 0
for i in range(N):
    ans += l%a[i]
print(ans)