n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=max(a[0]-x,0)
a[0]-=ans
for i in range(n-1):
  if a[i]+a[i+1]>x:
    ans+=a[i+1]+a[i]-x
    a[i+1]=x-a[i]
print(ans)