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
A = [0] + [int(input()) for _ in range(N)]

cur = 1
ans = 0
pushed = [False] * (N + 1)
pushed[1] = True
ok = True
while True:
    pushed[cur] = True
    ans += 1
    cur = A[cur]
    if cur == 2:
        break
    if pushed[cur]:
        ok = False
        break

if ok:
    print(ans)
else:
    print(-1)

        

