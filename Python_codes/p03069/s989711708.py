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
S = input()

acc_w = [0] * (N + 1)
acc_b = [0] * (N + 1)
for i in range(1, N + 1):
    c = S[i - 1]
    acc_w[i] = acc_w[i - 1] + (1 if c == '.' else 0)
    acc_b[i] = acc_b[i - 1] + (1 if c == '#' else 0)

ans = INF
for i in range(N + 1):
    now = acc_b[i] + acc_w[-1] - acc_w[i]
    ans = min(ans, now)
print(ans)




