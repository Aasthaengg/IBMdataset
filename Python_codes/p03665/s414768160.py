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
sys.setrecursionlimit(10 ** 6)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

n,p = I()
A = [2 if i%2==0 else 1 for i in I()]
a = set(A)



if p == 0:
    if len(a)==1 and 2 in a:
        print(2**n)
    else:
        print(2**(n-1))
else:
    if len(a)==1 and 2 in a:
        print(0)
    else:
        print(2**(n-1))