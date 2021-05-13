import numpy as np
N,M,C=map(int,input().split())
B=np.array(input().split(),dtype=np.int32)
A=np.array([input().split() for _ in range(N)],dtype=np.int32)

ans=((A*B).sum(axis=1)+C>0).sum()
print(ans)