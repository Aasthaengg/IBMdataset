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

N = i()
A = l()
ruiseki = [0]+list(itertools.accumulate(A))
i = bisect.bisect_left(ruiseki,sum(A)/2)
print(min(abs(sum(A[:i])-sum(A[i:])),abs(sum(A[:i-1])-sum(A[i-1:]))))
