import sys
input = sys.stdin.buffer.readline
import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
# print(f'{A=}, {A[1::2]=}')

M = [0] * N
M[0] = A.sum() - 2 * A[1::2].sum()

for i in range(N - 1):
    M[i + 1] = 2 * A[i] - M[i]

print(*M, sep=' ')
# A1 + A2 + ... + AN = X1 + X2 + ... + XN = S
# XN+1 = N1とすると
# (Xi + Xi+1) / 2 = Ai
# Xi + Xi+1 = 2 * Ai
# X1 = S - (X2 + ... + XN) = S - 2(A2 + A4 + ... + AN-1)
# Xi+1 = 2Ai - Xi
