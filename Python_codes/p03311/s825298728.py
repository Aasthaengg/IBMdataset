import numpy as np
N=int(input())
A=[int(i) for i in input().split()]
A=[A[i]-i for i in range(N)]
#print(A)
b=np.median(A)
K=[abs(A[i]-b) for i in range(N)]
print(int(sum(K)))