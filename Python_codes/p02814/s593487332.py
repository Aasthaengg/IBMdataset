from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
INF =  float("inf")
import bisect

N, M = list(map(int, input().split()))
a = list(map(int, input().split()))

# """nを素因数分解"""
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])
#
#     if temp!=1:
#         arr.append([temp, 1])
#
#     if arr==[]:
#         arr.append([n, 1])
#
#     return arr
#
# # 素因数分解に基づくlcm
# def fact_lcm(numbers):
#     d = defaultdict(int)
#     for a in numbers:
#         b = factorization(a)
#         for bb in b:
#             d[bb[0]] = max(d[bb[0]],bb[1])
#     return(dict(d))
#
# d = fact_lcm(a)
# c = 1
#
# for dd in d.items():
#     c *= dd[0]**dd[1]

# リストのlcm
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

c = lcm_list(a)

cc = c // 2

for aa in a:
    if cc % aa == 0:
        print(0)
        sys.exit()

print((M-cc) // c + 1)

