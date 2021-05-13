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
N = int(input())
A = [input() for _ in range(N)]
M = int(input())
B = [input() for _ in range(M)]

cnt_a = Counter(A)
cnt_b = Counter(B)

ans = 0
for k, v in cnt_a.items():
    val = v - cnt_b[k]
    ans = max(ans, val)
print(ans)
