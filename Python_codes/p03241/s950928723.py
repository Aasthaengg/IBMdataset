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

N, M = map(int, input().split())

i = 1

divs = []
while i ** 2 <= M:
    if M % i != 0:
        i += 1
        continue
    divs.append(i)
    divs.append(M // i)
    i += 1
divs = sorted(divs)
ans = 1
for d in divs:
    if N <= M // d:
        ans = max(d, ans)
print(ans)
