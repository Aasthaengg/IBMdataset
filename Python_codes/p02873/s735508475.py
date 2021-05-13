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
S = input()
S = S.replace('><', '>,<').split(',')
ans = 0
for w in S:
    a = w.count('<')
    b = w.count('>')
    mx = max(a, b)
    mn = min(a, b)
    ans += mx * (mx + 1) // 2 + (mn - 1) * mn // 2
print(ans)

