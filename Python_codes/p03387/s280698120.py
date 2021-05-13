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
cnt = 0
for i in range(1000):
    if A != B and B != C and A != C:
        A += 1
        B += 1
        C += 1
        if max(A,B,C) == A:
            A -= 1
        elif max(A,B,C) == B:
            B -= 1
        else:
            C -= 1
        cnt += 1
    if A == B and B == C and A == C:
        print(cnt)
        exit()
    if A == B or B == C or A == C:
        d = abs(max(A,B,C)-min(A,B,C))
        if [A,B,C].count(max(A,B,C)) == 2:
            if d%2 == 0:
                print(cnt+d//2)
                exit()
            else:
                print(cnt+d//2+2)
                exit()
        else:
            print(cnt+d)
            exit()