N,K=map(int,input().split())
A=list(map(int,input().split()))
F=list(map(int,input().split()))
A.sort(reverse=True)
F.sort()
import math
def isok(n):
  sum=0
  for i in range(N):
    sum+=max(0,A[i]-n//F[i])
  return sum<=K
ma=0
for i in range(N):
  ma=max(ma,A[i]*F[i])
start,end=-1,ma
while end-start>1:
  mid=(start+end)//2
  if isok(mid):
    end=mid
  else:
    start=mid
print(end)