import numpy as np
N=int(input())
A=np.array([int(i) for i in input().split()])
B=np.abs(A-np.mean(A))
print(np.argmin(B))