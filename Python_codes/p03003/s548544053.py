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
S = [0] + list(map(int, input().split()))
T = [0] + list(map(int, input().split()))
 
dp_cum = [[0] * (M+1) for _ in range(N+1)]
dp_cum[0][0] = 1
for n in range(N+1):
    dp_cum[n][0] = 1
for m in range(M+1):
    dp_cum[0][m] = 1
  
for n in range(1,N+1):
    for m in range(1,M+1):
        now = 0
        if S[n] == T[m]:
            now = dp_cum[n-1][m-1]
        dp_cum[n][m] = dp_cum[n-1][m] + dp_cum[n][m-1] - dp_cum[n-1][m-1] + now
        dp_cum[n][m] %= MOD
print(dp_cum[N][M]) 