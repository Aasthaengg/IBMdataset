import numpy as np

A=np.array([list(input()) for i in range(3)])
for i in range(3):
    print(np.diag(A)[i],end='')