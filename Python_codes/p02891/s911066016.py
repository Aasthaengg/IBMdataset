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
K = int(input())
ans = 0

S = list(S)
def f(T):
    ret = 0
    l = 0
    r = 1
    n = len(T)
    while l < n:
        while r < n and T[l] == T[r]:
            r += 1
        c = r - l
        ret += c // 2
        l = r
        r = l + 1
    return ret

first = f(S)
second = f(S + S)
diff = second - first

if len(set(S)) == 1:
    print(len(S) * K // 2)
else:
    print(first + diff * (K - 1))