import sys
import itertools
# import numpy as np
import time

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
for i in range(n):
    a[i], b[i] = (map(int, readline().split()))

a = sorted(a)
b = sorted(b)

if n % 2 == 0:
    n = n // 2
    l = (a[n - 1] + a[n])
    r = (b[n - 1] + b[n])
    print(r - l + 1)
else:
    n = n // 2
    l = a[n]
    r = b[n]
    print(r - l + 1)

