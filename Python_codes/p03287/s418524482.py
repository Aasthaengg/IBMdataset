import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,M = map(int,(input().split()))
A = list(map(int,(input().split())))
s = [0]*N
s[0] = A[0] % M
for i in range(1,N):
    s[i] = s[i-1] + A[i]
    s[i] %= M
d = defaultdict(int)
for i in s:
    d[i] += 1
ans = d[0]
for k in d.keys():
    ans += d[k]*(d[k]-1)//2

print(ans)