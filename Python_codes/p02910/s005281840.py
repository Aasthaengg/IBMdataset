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

s = s()

for i in range(len(s)):
    if (i+1) % 2 !=0:
        if s[i] == "R" or s[i]=="U" or s[i]=="D":
            pass
        else:
            print("No")
            sys.exit()
    else:
        if s[i]=="L" or s[i]=="U" or s[i]=="D":
            pass
        else:
            print("No")
            sys.exit()

print("Yes")