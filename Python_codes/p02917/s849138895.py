# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())
b = [1000000] + list(map(int, input().split())) + [1000000]

res = []

for i in range(n):
    res.append(min(b[i], b[i+1]))

print(sum(res))