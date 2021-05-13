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

Q = int(input())

MAX = 10 ** 5 + 2

is_prime = [True] * MAX

is_prime[0] = False
is_prime[1] = False
i = 2
while i ** 2 <= MAX:
    if is_prime[i]:
        for j in range(i * 2, MAX, i):
            is_prime[j] = False
    i += 1

count = [0] * MAX
for i in range(2, MAX):
    if is_prime[i] and is_prime[(i + 1) // 2]:
        count[i] = 1
ans = [0] * MAX
for i in range(1, MAX):
    ans[i] = ans[i - 1] + count[i - 1]

for i in range(Q):
    l, r = map(int, input().split())
    print(ans[r + 1] - ans[l])
