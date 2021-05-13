import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

L, R = map(int, input().split())

l = L % 2019

nums = set()
for i in range(min(R - L + 1, 2019)):
    nums.add((l + i) % 2019)
# print(l, r)
# if r <= l:
#     r += 2019
ans = 2018
for i in nums:
    for j in nums:
        if i == j:
            continue
        ans = min(ans, (i * j) % 2019)
print(ans)
