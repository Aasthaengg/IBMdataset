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
X = list(map(int, input().split()))

Y = [(i, x) for i, x in enu(X)]
sY = sorted(Y, key=lambda x: x[1])
ssY = [(i,) + y for i, y in enu(sY)]
sssY = sorted(ssY, key=lambda x: x[1])
# print(Y)
# print(sY)
# print(ssY)
# print(sssY)

for i in range(N):
    tup = sssY[i]
    sor_ind, ini_ind, val = tup
    # print(tup)
    if sor_ind < N//2:
        print(sY[N//2][1])
    else:
        print(sY[N//2-1][1])


