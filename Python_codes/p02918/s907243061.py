# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n, k = map(int, input().split())
s = input()

prev = ""
res = [0]
for i in range(1, n):
    if s[i] == s[i-1]:
        res.append(0)
    else:
        res.append(1)
# print(res)

ans = n - sum(res) - 1
ans += k*2
print(min(ans, n-1))
