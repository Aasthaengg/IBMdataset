import math
import numpy as np
N = int(input())
A = [int(_) for _ in input().split()]
B = [A[i] - i for i in range(N)]
B.sort()
C = np.array(B)
print(np.sum([abs(C[i]-C[math.floor(N/2)]) for i in range(N)]))