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

A, B = map(int, input().split())

cnt = 0
for num in range(A, B+1):
    num = str(num)
    if num[0]==num[-1] and num[1]==num[-2]:
        cnt += 1
print(cnt)