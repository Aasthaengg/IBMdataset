import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
A=[0]
for i in range(n):
  A.append(a[i]+A[-1])
l=0;r=10**10+1
while r-l>1:
  x=(l+r)//2
  ct=0
  for i in range(n):
    ct+=n-bisect.bisect_left(a,x-a[i])
  if ct<m:
    r=x
  else:
    l=x
ans=0
ct2=0
for i in range(n):
  y=bisect.bisect_left(a,l-a[i])
  ans+=A[n]-A[y]
  ans+=a[i]*(n-y)
  ct2+=n-y
print(ans-l*(ct2-m))