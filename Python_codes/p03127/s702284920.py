# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)
def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = z()
A = zz()
# A = sorted(A)
tmp =gcd(A[0], A[1])
for a in A[1:]:
    tmp = gcd(tmp, a)
ans = tmp
# for i in range(N):
#     for j in range(0, i):        
#         tmp = A[i] % A[j]
#         tmp = min(tmp, A[j]-tmp)
#         if (tmp != 0):
#             ans = min(ans, tmp)
print(ans)
            
