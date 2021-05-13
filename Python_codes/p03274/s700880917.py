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

N, K = map(int, input().split())
X = list(map(int, input().split()))

has_zero = 0 in X
negs = [val for val in X if val<0]
poss = [val for val in X if val>0]
lenn = len(negs)
lenp = len(poss)
negs.append(0)
poss = [0] + poss

# print(negs)
# print(poss)

minval = 10**9
if has_zero: K-=1
for left in range(0, K+1):
    right = K-left
    if lenn<left or lenp<right: continue
    # print(left, right)
    negv = abs(negs[lenn-left])
    posv = abs(poss[right])
    val = max(negv, posv) + 2*min(negv, posv)
    if val < minval: minval = val
print(minval)
