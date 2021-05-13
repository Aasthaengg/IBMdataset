import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N,H = map(int,(input().split()))
a = [[0]*2 for _ in range(N)]
for i in range(N):
    a[i] = list(map(int,(input().split())))
a.sort(key=lambda x:x[1],reverse=True)
M = max(a,key=lambda x:x[0])[0]

c = 0
for i in range(N):
    if a[i][1] > M:
        H -= a[i][1]
        c += 1
        if H <= 0:
            H = 0
            break
    else:
        break
c += math.ceil(H/M)
print(c)