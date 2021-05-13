import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = map(int, input().split())

ans = 0
MOD = 10 ** 9 + 7 
for i in range(k, n + 2):
    low = (0 + i - 1) * i // 2
    # high = sum(j for j in range(n + 1 - i, n + 1))
    high = (n + 1 - i + n) * i // 2
    ans += (high - low + 1) % MOD
print(ans % MOD)

