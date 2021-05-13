import numpy as np
N = int(input())
D,X = map(int, input().split())
A = np.array([int(input()) for _ in range(N)])

A = (D-1)//A + 1
print(A.sum() + X)