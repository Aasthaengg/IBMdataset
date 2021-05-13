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
S = [0] * N
for i in range(N):
    s, t = input().split()
    S[i] = (s, int(t))
X = input()

cnt = False
ans = 0
for s, t in S:
    if s == X:
        cnt = True
    elif cnt:
        ans += t

print(ans)