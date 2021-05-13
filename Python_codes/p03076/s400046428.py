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
A = [int(input()) for _ in range(5)]

def calc(p):
    t = 0
    for n, i in enumerate(p):
        t += A[i]
        if n == 4:
            break
        r = t % 10
        t += (10 - r) % 10
    return t

ans = INF
for p in permutations(range(5)):
    ans = min(calc(p), ans)
print(ans)

