import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, Q = map(int, input().split())
events = []
for i in range(N):
    s, t, x = map(int, input().split())
    events.append((s - x, 0, x))
    events.append((t - x, 1, x))

for i in range(Q):
    d = int(input())
    events.append((d, 2, i))

events = sorted(events)

q = [INF]
cnt = defaultdict(int)
cnt[INF] = 1
ans = [INF] * Q
for a, b, c in events:
    if b == 0:
        heapq.heappush(q, c)
        cnt[c] += 1
    if b == 1:
        cnt[c] -= 1
    if b == 2:
        while cnt[q[0]] == 0:
            heapq.heappop(q)
        if q[0] == INF:
            ans[c] = -1
        else:
            ans[c] = q[0]
for i in range(Q):
    print(ans[i])