X, N = list(map(int,input().split()))
L = list(map(int,input().split()))

import numpy as np

l = np.cumsum(L)

print(len(l[l<=N])+1)