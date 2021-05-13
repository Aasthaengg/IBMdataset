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
m1 = A*B
m2 = B*C
m3 = A*C
t1 = abs(m1*(C//2)-m1*(C-C//2))
t2 = abs(m2*(A//2)-m2*(A-A//2))
t3 = abs(m3*(B//2)-m3*(B-B//2))
print(min(t1,t2,t3))
