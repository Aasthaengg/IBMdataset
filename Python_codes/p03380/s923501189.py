import numpy as np


n = int(input())
A = np.array(sorted(map(int, input().split())))

a = A[-1]
A = A[:-1]
i = np.argsort(np.abs(A - a / 2))[0]
b = A[i]

print(a, b)