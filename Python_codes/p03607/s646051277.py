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

N = int(input())
A = Counter([int(input()) for _ in range(N)])
ans = 0
for k, v in A.items():
    if v % 2 == 1:
        ans += 1
print(ans)


