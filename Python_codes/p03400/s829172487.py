import math
N=int(input())
D,X=map(int,input().split())
choco=[0]*D
ans=0
for _ in range(N):
  A=int(input())
  ans+=math.ceil(D/A)
print(ans+X)


