#!/usr/bin/env python3

import heapq

n, m, *a = map(int, open(0).read().split())

a = [*map(lambda x: -x, a)]
heapq.heapify(a)
for _ in range(m):
    heapq.heappush(a, -(-heapq.heappop(a) >> 1))
print(-sum(a))
