from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
from fractions import gcd

NN = 202020
MOD = 10**9+7
INF = float("inf")

n = int(input())
A = list(map(int, input().split()))

init_pos = 0
psum = 0
for i in range(n):
    psum += A[i]
    if i%2 == 0 and psum <= 0:
        init_pos += 1-psum
        psum = 1
    elif i%2 == 1 and psum >= 0:
        init_pos += psum + 1
        psum = -1

init_neg = 0
psum = 0
for i in range(n):
    psum += A[i]
    if i%2 == 1 and psum <= 0:
        init_neg += 1-psum
        psum = 1
    elif i%2 == 0 and psum >= 0:
        init_neg += psum + 1
        psum = -1

print(min(init_pos, init_neg))
