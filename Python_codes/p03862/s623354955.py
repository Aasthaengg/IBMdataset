import sys
n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n-1):
  if a[i]+a[i+1]>x:
    if a[i]<x:
      ans+=a[i]+a[i+1]-x
      a[i+1]=x-a[i]
    else:
      ans+=a[i]+a[i+1]-x
      a[i+1]=0
print(ans)