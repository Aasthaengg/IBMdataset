# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = sum(b)
prev = -10
for i in range(n):
    if i > 0:
        if a[i] == a[i-1]+1:
            ans += c[a[i-1]-1]
    prev = a[i]

print(ans)