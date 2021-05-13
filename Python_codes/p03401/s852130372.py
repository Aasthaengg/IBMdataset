import numpy as np
N = int(input())
A = np.array(["0"] + input().split() + ["0"], dtype=np.int64)
B = np.abs(A[1:] - A[:-1])
C = np.abs(A[2:] - A[:-2])
D = B[1:] + B[:-1]
total = B.sum()
for i in range(N):
    print(total - D[i] + C[i])