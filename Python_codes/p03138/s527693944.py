# なぜかうまくいかない
import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_right, bisect_left

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()    
A = LIST()
# 2 ** 40 > 10 ** 12 ?
tmp = [0] * 40

for a in A:
    for i in range(40):
        if a & (1 << i):
            tmp[i] += 1

# 解説のx
x = 0

for i in range(39, -1, -1):
    # 大きい順にK以下に収めていくのがコツ
    # 2 ** i
    # K以下である かつ tmp[i]の1の数が0の数より小さいなら，
    # 和はより大きくなるので変える
    if x + (1 << i) <= K and tmp[i] < (N + 1) // 2:
        x += (1 << i)
        # x = 11010101...みたいな長さ40のものが出来上がる
# この x が，f(x)を最大とするx
# あとはf(x)をだすだけ
# print(a)
ans = 0
for i in A:
    ans += i ^ x
print(ans)