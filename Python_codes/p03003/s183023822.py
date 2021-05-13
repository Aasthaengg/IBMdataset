import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

S.append(0)
T.append(0)
MAX = 2005
dp0 = [[0] * MAX for _ in range(MAX)]
dp1 = [[0] * MAX for _ in range(MAX)]

dp0[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        dp0[i + 1][j] += dp0[i][j] % MOD
        dp1[i][j] += dp0[i][j] % MOD
        dp1[i][j + 1] += dp1[i][j] % MOD
        if S[i] == T[j]: 
            dp0[i + 1][j + 1] += dp1[i][j] % MOD
print(dp1[N][M] % MOD)
