import numpy as np

N = int(input())
A = np.array([int(input()) for _ in range(N)] + [0], dtype='int64')

x = (A[:-1][A[:-1] >= A[1:]]).sum()

if A[0] != 0:
    x = -1
if (A[1:] >= A[:-1] + 2).any():
    x = -1

print(x)
