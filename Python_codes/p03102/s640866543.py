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
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

N, M, C = I()
que = []
B = l()
A = []
for i in range(N):
    a = l()
    A.append(a)

count = 0
for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j]*B[j]
    ans += C
    if ans > 0:
        count += 1

print(count)
