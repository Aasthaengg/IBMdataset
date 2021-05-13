import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
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
cnt = 0
ans = 0
inf = float("inf")

n = k()
s = s()
r = s.count("R")
g = s.count("G")
b = s.count("B")
ans = r*g*b
for i in range(n-2):
    for j in range((n-i+1)//2):
        if s[i]!=s[i+j] and s[i+j]!=s[i+2*j] and s[i+2*j]!=s[i]:
            ans-=1

print(ans)
