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
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0
inf = float("inf")

l,r = I()

if r-l >= 673:
    print(0)
    exit()
ans = 2018
for i in range(l,r):
    for j in range(i+1,r+1):
        ans = min(ans,i*j%2019)

print(ans)
