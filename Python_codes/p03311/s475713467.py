import numpy as np

N = int(input())
A = np.array(list(map(int,input().split())))
A -= np.arange(1,N+1)
print(sum(abs(A-int(np.median(A)))))