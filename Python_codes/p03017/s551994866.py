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
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

N,A,B,C,D = I()
S = s()
if "##" in S[A-1:C] or "##" in S[B-1:D]:
    print("No")
else:
    if C > D and "..." not in S[B-2:D+1]:
        print("No")
    else:
        print("Yes")
