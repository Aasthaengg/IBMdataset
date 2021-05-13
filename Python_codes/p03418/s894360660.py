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

cnt = 0
for b in range(max(1, K), N+1):
    cnt += N-max(1, K)+1
    if b!=0:
        cnt -= K*(N//b)
        if b*(N//b)+(K-1) > N:
            cnt += b*(N//b)+(K-1) - N

print(cnt)

