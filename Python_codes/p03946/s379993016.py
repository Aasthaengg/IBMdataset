import numpy as np
N,T = map(int,input().split())
A=np.array(input().split(),dtype=np.int32)
s=A-np.minimum.accumulate(A)
print((s==max(s)).sum())
