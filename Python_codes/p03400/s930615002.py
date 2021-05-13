import math
N=int(input())
D,X=map(int,input().split())
A=[0]*N
ans=X
for i in range(N) :
  A[i]=int(input())
for i in range(N) :
  ans+=1+math.floor((D-1)/A[i])
print(ans)