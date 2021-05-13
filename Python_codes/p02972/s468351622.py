import sys
import numpy as np
input = sys.stdin.buffer.readline
N = int(input())
A = np.array(list(map(int, input().split())))

B = np.array([0] * N)
for i in range(len(A), 0, -1):
    v = B[2 * i - 1::i].sum() % 2
    if A[i - 1] != v:
        B[i - 1] = 1
# print(f'{B=}')

M = B.sum()
print(M)
idx = np.where(B == 1)[0] + 1
print(*idx, sep=' ')
