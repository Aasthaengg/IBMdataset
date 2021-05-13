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
A = list(map(int, input().split()))
A = [0] + A + [0]

dist = 0
difs = [0]*N
for i, a in enu(A[:-2]):
    c = a
    n = A[i+1]
    nn = A[i+2]
    dist += abs(n-c)

    dif = 0 # 消したときに減る量
    flg_dif = (c<=n)^(n<=nn)
    if flg_dif:
        difs[i] = min(2*abs(n-c), 2*abs(nn-n))
dist += abs(A[-2])

# print('dist', dist)
# print('difs', difs)
for i, a in enu(A[1:-1]):
    print(dist-difs[i])
