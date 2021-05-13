import sys
import math
import itertools
import collections
import numpy as np

rl = sys.stdin.readline

def a():
    N, M = map(int, rl().split())
    li = [[] for _ in range(N)]
    deg = [0] * N
    for _ in range(M):
        a, b = map(int, rl().split())
        a -= 1
        b -= 1
        li[a].append(b)
        deg[b] += 1
    d = collections.deque([i for i in range(N) if deg[i] == 0])
    dp = [0] * N
    while d:
        i = d.popleft()
        for j in li[i]:
            deg[j] -= 1
            if deg[j] == 0:
                dp[j] = max(dp[j] ,dp[i] + 1)
                d.append(j)
    print(max(dp))
a()




        


