import re
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

S = X()
p = set(S)
if len(S) == 1:
    print("YES")
    sys.exit()

if len(p) == 1:
    print("NO")
    sys.exit()

a = S.count("a")
b = S.count("b")
c = S.count("c")
cnt = len(S)//3

if len(S) % 3 == 0:
    if a <= cnt and b <=cnt and c<= cnt:
        print("YES")
    else:
        print("NO")
else:
    if a <= cnt+1 and b <=cnt+1 and c<= cnt+1:
        print("YES")
    else:
        print("NO")
