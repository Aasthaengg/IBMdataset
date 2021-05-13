import numpy as np

N, M, X = map(int, input().split())
A = np.array(list(map(int, input().split())))
if len(A[A < X]) > len(A[A > X]):
    print(len(A[A > X]))
else:
    print(len(A[A < X]))