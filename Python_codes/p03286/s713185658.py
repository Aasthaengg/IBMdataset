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
if N == 0:
    print('0')
    exit()

ans = ''
while abs(N) > 0:
    if abs(N) % 2 == 0:
        ans += '0'
        N //= 2
    elif N < 0:
        N = (N - 1) // 2
        ans += '1'
    else:
        ans += '1'
        N //= 2
    N *= -1
print(ans[::-1])



