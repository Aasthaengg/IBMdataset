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

N, K = map(int, input().split())
S = input()

prev = S[0]
i = 0
count = 0
run_length = []
if S[0] == '0':
    run_length.append(0)
while i < len(S):
    c = S[i]
    if c == prev:
        count += 1
    else:
        run_length.append(count) 
        count = 1
    prev = c
    i += 1
run_length.append(count) 

acc = [0] * (len(run_length) + 1)
acc[0] = 0

for i in range(len(acc) - 1):
    acc[i + 1] = acc[i] + run_length[i]

ans = 0
for i in range(0, len(acc), 2):
    j = 2 * K + 1
    x = 0
    if j + i >= len(acc):
        x = acc[-1] - acc[i]
    else:
        x = acc[j + i] - acc[i]
    ans = max(ans, x)

# for i in range(0, len(run_length), 2):
#     ans = max(ans, run_length[i])
# print(acc)
print(ans)


