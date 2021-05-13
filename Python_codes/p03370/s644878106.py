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

N, X = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

minm = MOD
for mi in m:
    minm = min(minm, mi[0])
    X -= mi[0]
print(N + X//minm)