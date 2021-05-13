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
mod = 10**9+7

A,B,C = I()
if max(A,B,C) == A:
    print(A*10+B+C)
elif max(A,B,C) == B:
    print(B*10+A+C)
else:
    print(C*10+A+B)