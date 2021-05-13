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

n = int(input())
A = map(int, input().split())

x = 1
for a in A:
    if a == x:
        x += 1

if x == 1:
    print(-1)
else:
    print(n - x + 1)

