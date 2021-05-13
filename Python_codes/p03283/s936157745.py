import sys
import numpy as np
from itertools import accumulate

input = sys.stdin.readline

N, M, Q = map(int, input().split())

lines = np.zeros((501, 501), np.int32)

for _ in range(M):
    l, r = map(int, input().split())
    lines[l, r] += 1

lines = np.cumsum(lines, axis = 0)
lines = np.cumsum(lines, axis = 1)


for _ in range(Q):
    p, q = map(int, input().split())
    print(lines[-1, q] - lines[p-1, q])