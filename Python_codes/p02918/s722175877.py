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

N, K = map(int, readline().split())
S = readline().decode()
prev = ''
total = 0
for c in S:
    if prev == c:
        total += 1
    prev = c

print(min(N - 1, total + K * 2))
