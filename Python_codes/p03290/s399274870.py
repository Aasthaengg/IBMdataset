#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime

# atcoder.main
# Date: 2020/06/20
# Filename: main 
# Author: acto_mini

sys.setrecursionlimit(10 ** 8)
INF = float('inf')

D, G = map(int, input().split())
ans = INF
PC = [list(map(int, input().split())) for i in range(D)]

for bit in range(1 << D):
    count = 0
    sum = 0
    left_over = set(range(1, D + 1))

    for i in range(D):
        if bit & (1 << i):
            sum += PC[i][0] * (i + 1) * 100 + PC[i][1]
            count += PC[i][0]
            left_over.discard(i + 1)

    if sum < G:
        use = max(left_over)
        n = min(PC[use - 1][0], -(-(G - sum) // (use * 100)))
        count += n
        sum += n * use * 100

    if sum >= G:
        ans = min(ans, count)

print(ans)
