import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

S = input()
count = [0] * 26
for c in S:
    count[ord(c) - ord('a')] += 1

n = len(S)
ans = n * (n - 1) // 2 + 1
for c in count:
    ans -= c * (c - 1) // 2
print(ans)

