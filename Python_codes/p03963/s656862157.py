import itertools
import math
import sys
import heapq
from collections import Counter
from collections import deque
from fractions import gcd
INF = 1 << 60
sys.setrecursionlimit(10 ** 6)

#ここから書き始める
n, k = map(int, input().split())
ans = k
if n >= 2:
    ans = k * (k - 1) ** (n - 1)
print(ans)