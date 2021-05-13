import numpy as np
A, B = input().split(' ')
A = int(A)
B = int(B)
print(int(np.ceil((B - 1) / (A - 1))))