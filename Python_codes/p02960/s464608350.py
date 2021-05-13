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

s = input()
s = list(reversed(s))

mods = [0 for _ in range(13)]
mods[0] = 1

x = 1
MOD = 10 ** 9 + 7
for c in s:
    new_mods = [v for v in mods]
    val = 0
    if c == '?':
        for i in range(1, 10):
            val = i * x % 13
            for j in range(13):
                new_mods[j] += mods[j - val] % MOD
    else:
        val = int(c) * x % 13
        for i in range(13):
            new_mods[i] = mods[i - val] % MOD

    mods = new_mods
    # print(mods)
    x *= 10
    x %= 13
print(mods[5] % MOD)
# print(total_mod % 13)

