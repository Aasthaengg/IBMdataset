import numpy as np
N = int(input())
A = list(map(int,input().split()))
X =[0]*N
sum_=0
for i in range(N):
  if i%2==0:
    sum_=sum_+A[i]
  else:
    sum_=sum_-A[i]
X[0]=int(sum_/2)
for i in range(1,N):
  X[i]=A[i-1]-X[i-1]
X = list(np.array(X)*2)
print(*X)