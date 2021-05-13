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

a,b,c,d = I()
x = lcm(c,d)

if a == b:
    if a % c != 0 and a % d != 0:
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()

aa = a-1+(a-1)//x - (a-1)//c - (a-1)//d
bb = b+b//x - b//c - b//d
ans = bb-aa

print(ans)
