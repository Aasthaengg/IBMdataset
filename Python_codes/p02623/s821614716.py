n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0

A,B=[0],[0]
for i in range(n):
  A.append(a[i]+A[i])
for i in range(m):
  B.append(b[i]+B[i])

for j in range(n+1):
  K=k-A[j]
  if K<0:
    break
  left=0
  right=m+1
  while left<right:
    mid=(left+right)//2
    if B[mid]>K:
      right=mid
    else:
      left=mid+1
  ans=max(ans,j+left-1)
print(ans)
