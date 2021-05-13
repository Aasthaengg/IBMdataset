#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left, bisect_right #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

res = -10**12
for i in range(1, 2**10):
    tres = 0
    cnts = [0]*N
    for j in range(10):
        bo = (i>>j) & 1
        for k in range(N):
            cnts[k] += F[k][j] & bo
    for k in range(N):
        tres += P[k][cnts[k]] 
    if res < tres:
        res = tres
print(res)
