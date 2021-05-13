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
a, b, x = map(int, input().split())
if a <= x <= a + b:
    print("YES")
else:
    print("NO")