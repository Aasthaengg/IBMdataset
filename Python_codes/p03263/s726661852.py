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
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

h,w = I()
A = []
for i in range(h):
    A.append([int(i) for i in input().split()])
Ans = []
for i in range(h):
    for j in range(w-1):
        if A[i][j] % 2==1:
            Ans.append([i+1,j+1,i+1,j+2])
            A[i][j+1] += 1

for i in range(h-1):
    if A[i][w-1] % 2 == 1:
        Ans.append([i+1,w,i+2,w])
        A[i+1][w-1] += 1

print(len(Ans))
for ans in Ans:
    print(*ans)