#coding: utf-8
import math
import heapq
import bisect
from collections import Counter, deque
import itertools
#from scipy.misc import comb

MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
A.sort()

c = sorted(list(Counter(A).items()))

ans = 1
if N%2 == 1:
    for i in range(len(c)):
        if i==0:
            if c[i][0] == 0 and c[i][1] == 1:
                ans = 1
            else:
                ans = 0
        else:
            if c[i][0] == i*2 and c[i][1] == 2:
                ans *= 2
                ans %= MOD
            else:
                ans = 0
else:
    for i in range(len(c)):
        if c[i][0] == i*2+1 and c[i][1] == 2:
            ans *= 2
            ans %= MOD
        else:
            ans = 0

print(ans)