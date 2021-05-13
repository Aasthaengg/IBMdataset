import numpy as np

N=int(input())
A=np.array(list(map(int, input().split())))
S=sum(A)-A[0]
X=A[0]
ans=abs(S-X)
for i in range(1,N-1):
  X+=A[i]
  S-=A[i]
  ans=min(ans,abs(S-X))
print(ans)