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
N, M = map(int, input().split())
S = input()
T = input()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
lcm = N * M // gcd(N, M)
# SとTそれぞれindexが何個進むとlcm番目の文字が出現するか求める
si = lcm // M
ti = lcm // N

i = 0
j = 0
ok = True
while i < N and j < M:
    if S[i] != T[j]:
        ok = False
        break
    i += si
    j += ti
if ok:
    print(lcm)
else:
    print(-1)