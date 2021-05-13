import sys
input = sys.stdin.readline

import numpy as np

N = int(input())
A = np.array([int(input()) for x in range(N)] + [0], dtype=np.int64)

x = (A[:-1][A[:-1] >= A[1:]]).sum()

if (A > np.arange(len(A))).any():
    x = -1
if (A[1:] >= A[:-1] + 2).any():
    x = -1

print(x)