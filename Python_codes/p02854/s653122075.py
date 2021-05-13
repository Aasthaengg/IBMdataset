import numpy as np

N = int(input())
A = [int(x) for x in input().split()]
A = np.array(A)

Acum = A.cumsum()
L = Acum[:-1]
R = Acum[-1] - L
print(abs(L-R).min())