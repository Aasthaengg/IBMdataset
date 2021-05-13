import numpy as np

N = int(input())
A = list(map(int, input().split()))

A = np.array(A)
B = 1 / A
C = B.sum()
print(1/C)