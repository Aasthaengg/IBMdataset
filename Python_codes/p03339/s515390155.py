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
def pri(x): print('\n'.join(map(str, x)))

N = int(input())
S = input()

wl = [0]*N
el = [0]*N
wr = [0]*N
er = [0]*N

if S[0] == 'W':
    wl[0] = 1
    el[0] = 0
else:
    wl[0] = 0
    el[0] = 1

if S[-1] == 'W':
    wr[0] = 1
    er[0] = 0
else:
    wr[0] = 0
    er[0] = 1

for i in range(1, N):
    if S[i] == 'W':
        wl[i] = wl[i-1] + 1
        el[i] = el[i-1]
    else:
        wl[i] = wl[i-1]
        el[i] = el[i-1] + 1

    if S[-i-1] == 'W':
        wr[i] = wr[i-1] + 1
        er[i] = er[i-1]
    else:
        wr[i] = wr[i-1]
        er[i] = er[i-1] + 1

# print(wl)
# print(el)
# print(wr)
# print(er)

res = N
for i in range(N):
    if i == 0:
        val = er[N-i-1]
    elif i == N-1:
        val = wl[i-1] 
    else:
        val = wl[i-1] + er[N-i-1]
    # print(i, val)
    if res > val:
        res = val

print(res)
