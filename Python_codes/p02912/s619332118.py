#!/usr/bin/env python3

from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [-1*item for item in a]
heapify(a)

for i in range(m):
    max = -1* heappop(a)
    heappush(a, int(-1*max/2))  # 要素の挿入

a = [-1*item for item in a]
ans = sum(list(a))

print(ans)
