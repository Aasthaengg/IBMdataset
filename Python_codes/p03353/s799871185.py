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
K = int(input())

d = sorted(list(S))
x = set(d)
for c in d:
    left = S.index(c)
    while left < len(S):
        if S[left] != c:
            left += 1
            continue
        j = 2
        while j <= K:
            x.add(S[left:left+j])
            j += 1
        left += 1
    if len(x) >= K:
        break
x = sorted(list(x))
print(x[K - 1])