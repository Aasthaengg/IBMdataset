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

n,m = I()
num = [l() for i in range(m)]
a = [-1]*n
for i in num:
    if a[i[0]-1] != -1:
        if a[i[0]-1] == i[1]:
            pass
        else:
            print(-1)
            sys.exit()
    else:
        a[i[0]-1] = i[1]

if n == 1:
    if a[0] == -1:
        print(0)
        sys.exit()
    else:
        print(a[0])
        sys.exit()

if a[0] == 0:
    print(-1)
else:
    a = [0 if i == -1 else i for i in a]
    if a[0] == 0:
        a[0] =1
    print("".join(map(str,a)))
