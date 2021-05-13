import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

import itertools

n = int(readline())
a = sorted(tuple(map(int, readline().split())))
cnt = 1
cumsum = list(itertools.accumulate(a))
for i in range(1, n):
    if cumsum[i - 1] * 2 < a[i]:
        n -= cnt
        cnt = 0
    cnt += 1
print(n)
