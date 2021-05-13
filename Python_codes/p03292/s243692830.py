#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

A = list(map(int, input().split()))
A.sort()
rA = list(reversed(A))

res = 10000
val = 0
for i in range(2):
    val += A[i+1] - A[i]
res = min(res, val)
for i in range(2):
    val += abs(rA[i+1] - rA[i])
res = min(res, val)
print(res)