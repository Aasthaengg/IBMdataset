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

n = k()
p = l()
for i in range(1,n-1):
    a = []
    a.append(p[i-1])
    a.append(p[i])
    a.append(p[i+1])
    a.sort()
    if a.index(p[i]) == 1:
        count += 1

print(count)
