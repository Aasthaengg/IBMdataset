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
N, K = map(int, input().split())

adj = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

from collections import deque
q = deque([])
q.append(0)
ps = [0] * N
ps[0] = K
visited = [False] * N
visited[0] = True
while len(q) > 0:
    v = q.popleft()
    now = K - 2
    if v == 0:
        now = K - 1
    for u in adj[v]:
        if visited[u]:
            continue
        visited[u] = True
        ps[u] = now
        now -= 1
        q.append(u)
ans = 1
for p in ps:
    ans *= p
    ans %= MOD
print(ans % MOD)

