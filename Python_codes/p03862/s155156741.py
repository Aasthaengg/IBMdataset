n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0

z=a[0]+a[1]-x
if z>0:
  ans+=z
  a[1]-=z
  if a[1]<0:
    a[0]-=abs(a[1])
    a[1]=0

for i in range(n-1):
  z=a[i]+a[i+1]-x
  if z>0:
    ans+=z
    a[i+1]-=z
    if a[i+1]<0:
      a[i]-=abs(a[i+1])
      a[i+1]=0

print(ans)