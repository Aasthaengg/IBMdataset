import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

while(len(np.nonzero(A)[0]) != 1):
    devisor = np.min(A[np.nonzero(A)])
    devisor_i = np.where(A==devisor)[0][0]
    A = np.array([A[devisor_i], *(A%devisor)[:devisor_i], *(A%devisor)[devisor_i+1:]])
    
print(*A[np.nonzero(A)])