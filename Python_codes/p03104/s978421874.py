import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heapify, heappop, heappush
 
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

A, B = MAP()

def f(X):
    if X % 2 == 1:
        one_num = (X + 1) // 2
        if one_num % 2 == 0:
            return 0
        else:
            return 1
    else:
        one_num = X // 2
        if one_num % 2 == 0:
            return 0 ^ X
        else:
            return 1 ^ X
print(f(B) ^ f(A-1))

