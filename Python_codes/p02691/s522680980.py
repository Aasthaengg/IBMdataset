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

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
res = 0
for i, a in enu(A):
    v1 = i+a
    v2 = i-a
    res += d[v2]
    d[v1] += 1
print(res)