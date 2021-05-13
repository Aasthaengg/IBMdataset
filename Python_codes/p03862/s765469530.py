N,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
ans=0
for i in range(N):
  if i==0:
    if a[i]+a[i+1]>x:
      if a[i]>x:
        ans+=a[i+1]+a[i]-x
        a[i+1]=0
      else:
        ans+=(a[i]+a[i+1]-x)
        a[i+1]=x-a[i]
  else:
    if a[i]+a[i+1]>x:
      if a[i]>x:
        ans+=a[i+1]+a[i]-x
        a[i+1]=0
      else:
        ans+=(a[i]+a[i+1]-x)
        a[i+1]=x-a[i]
print(ans)