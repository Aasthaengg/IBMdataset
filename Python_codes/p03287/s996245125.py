import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools
from collections import Counter

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
a[0] %= m
cumsum = list(itertools.accumulate(a, lambda x, y: (x + y) % m))
counter = list(Counter(cumsum).items())
cnt = 0
for i, v in counter:
    cnt += v * (v - 1) // 2
    if i == 0:
        cnt += v
print(cnt)
