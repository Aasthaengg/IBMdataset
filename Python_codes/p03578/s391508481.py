import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

cnt_d = Counter(D)
cnt_t = Counter(T)

for k, v in cnt_t.items():
    cnt_d[k] -= v
    if cnt_d[k] < 0:
        print("NO")
        exit()
print("YES")