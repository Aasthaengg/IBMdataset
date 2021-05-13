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
x = [[] for _ in range(N)]
for i in range(N):
    x[i] = list(map(int,(input().split())))
y = copy.deepcopy(x)

ans = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            if i == 1:
                for l in range(N):
                    y[l][0] = -x[l][0]
            else:
                for l in range(N):
                    y[l][0] = x[l][0]
            if j == 1:
                for l in range(N):
                    y[l][1] = -x[l][1]
            else:
                for l in range(N):
                    y[l][1] = x[l][1]
            if k == 1:
                for l in range(N):
                    y[l][2] = -x[l][2]
            else:
                for l in range(N):
                    y[l][2] = x[l][2]
            s = [-1]*N
            for l in range(N):
                s[l] = sum(y[l])
            s.sort(reverse=True)
            ans = max(ans,sum(s[:M]))
print(ans)