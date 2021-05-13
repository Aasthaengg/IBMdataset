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

S = s()
n = len(S)
num = 1
num2 = 1
ans = 0
Flag = 0

for i in range(n-1):
    if S[i] == S[i+1]:
        ans += num
        num += 1
    if S[i] == "<" and S[i+1] == ">":
        num2 = num
        num = 1
        Flag = 1
    if S[i] == ">" and S[i+1] == "<":
        ans += max(num,num2)
        num = 1
        Flag = 0

if Flag:
    ans += max(num,num2)
else:
    ans += num

print(ans)
