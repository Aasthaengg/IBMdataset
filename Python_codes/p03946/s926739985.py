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

N,T = map(int,(input().split()))
a = list(map(int,(input().split())))
a.append(0)
m = a[0]
p = []
for i in range(1,N):
    if m < a[i] > a[i+1]:
        M = a[i]
        p.append(M-m)
    elif a[i] < m:
        m = a[i]

ans = p.count(max(p))
print(ans)