n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
ans=0
for i in range(1,n+1):
  if a[i]+a[i-1]>x:
    ans=ans+a[i]+a[i-1]-x
    a[i]=a[i]-(a[i]+a[i-1]-x)
print(ans)