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

N = int(input())
S = [0] * 2
S[0] = input()
S[1] = input()

ans = 1
prev = 1 # 1 = vertical, 2 = horizontal
i = 0
if S[0][0] == S[1][0]:
    ans *= 3
    i += 1
    prev = 1
else:
    ans *= 6
    i += 2
    prev = 2

while i < N:
    if S[0][i] == S[1][i]:
        if prev == 1:
            ans *= 2 
        else:
            ans *= 1
        i += 1
        prev = 1
    else:
        if prev == 2:
            ans *= 3
        else:
            ans *= 2 
        i += 2
        prev = 2
    ans %= MOD
print(ans)