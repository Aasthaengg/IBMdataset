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

n = input()
n = reversed(n)

x = 1
count = [0 for _ in range(2019)]
MOD = 2019
acc = 0
count[0] = 1
ans = 0

for c in n:
    a = x * int(c)
    acc += a
    acc %= MOD
    ans += count[acc]
    count[acc] += 1
    x = (x * 10) % MOD

print(ans)
