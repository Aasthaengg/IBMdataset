import numpy as np
N = int(input())
T, A = [int(i) for i in input().split()]
H = np.array([int(i) for i in input().split()])
print(np.argmin(np.abs(T - H*0.006 - A))+1)