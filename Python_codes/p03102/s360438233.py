import numpy as np
N,M,C=map(int,input().split())
B=np.array(input().split(),dtype=np.int32)
ans=0
for _ in range(N):
    A=np.array(input().split(),dtype=np.int32)
    if A.dot(B)+C>0:
        ans+=1
print(ans)
