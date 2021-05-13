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
INF = 10**9
mod = 10**9+7

A,B = I()
ans = 0
for i in range(A,B+1):
    F = 1
    s = str(i)
    for i in range(2):
        if s[i] != s[4-i]:
            F = 0
    if F == 1:
        ans += 1
print(ans)