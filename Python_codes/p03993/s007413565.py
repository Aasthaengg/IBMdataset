import numpy as np

N = int(input())
A = np.array(tuple(map(int, input().split())))
print(np.count_nonzero(A[A - 1] == np.arange(N) + 1) // 2)
