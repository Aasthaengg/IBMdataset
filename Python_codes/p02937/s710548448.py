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

s = list(input().rstrip())
t = list(input().rstrip())

d = {}
N = len(s)
for i in range(N):
    if s[i] not in d:
        d[s[i]] = [i]
    else:
        d[s[i]].append(i)

now = -1
c = 0
for i in range(len(t)):
    if t[i] in d:
        next = bisect.bisect_right(d[t[i]],now)
        if next < len(d[t[i]]):
            nnum = d[t[i]][next]
            now = nnum
        else:
            c += 1
            now = -1
            next = bisect.bisect_right(d[t[i]],now)
            nnum = d[t[i]][next]
            now = nnum
    else:
        print(-1)
        break
else:
    print(c*N+now+1)