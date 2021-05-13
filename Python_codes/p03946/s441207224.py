import numpy as np
N,T = map(int,input().split())
A = list(map(int,input().split()))
C = np.array(A)-np.minimum.accumulate(A)
print(sum(C==max(C)))