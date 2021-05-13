n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans,right=0,0

A,B=[0],[0]
for i in range(n):
  A.append(a[i]+A[i])
for i in range(m):
  B.append(b[i]+B[i])
for i in range(m+1):
  if k<B[i] or i==m:
    right=i-1
    if i==m:
      right=i
    ans=right
    break

for j in range(0,n):
  if k<a[j]:
    break
  k-=a[j]
  while k<B[right]:
    right-=1
  ans=max(ans,right+j+1)
print(ans)