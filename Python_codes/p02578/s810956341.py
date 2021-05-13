# C - Step
import numpy as np

N = int(input())
A = np.array([int(a) for a in input().split()])
Amax = np.maximum.accumulate(A)

print(sum(Amax-A))