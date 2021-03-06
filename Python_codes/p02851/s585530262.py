# -*- coding: utf-8 -*-
# E

from collections import defaultdict
from itertools import accumulate
from collections import deque

N, K = map(int, input().split())
a = list(map(int, input().split()))
a = [a-1 for a in a]
# print(a)

s = [0] + list(accumulate(a))
# print(s)
s = [s % K for s in s]
# print(s)

d = defaultdict(int)
queue = deque()

ans = 0
for idx, s in enumerate(s):
    queue.append(s)
    if idx >= K:
        s_prev = queue.popleft()
        d[s_prev] -= 1

    ans += d[s]
    d[s] += 1
    # print(d)

print(ans)
