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

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
A = list(map(int, input().split()))

if A[0] != 0:
    print(0)
    exit()

MAX = 2 * 10 ** 5 + 5
count = [0] * N
count[0] = 1
ans = 3
MOD = 10 ** 9 + 7
for a in A[1:]:
    if a == 0:
        ans *= 3 - count[0]
    else:
        ans *= count[a - 1] - count[a]
    ans %= MOD
    count[a] += 1

print(ans % MOD)