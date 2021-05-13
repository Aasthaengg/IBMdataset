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
pri = lambda x: print(*x, sep='\n')

s = input()
K = int(input())

subs = set()
for i in range(len(s)):
    for l in range(1, K+1):
        subs.add(s[i:i+l])
opt = sorted(list(subs))
print(opt[K-1])

