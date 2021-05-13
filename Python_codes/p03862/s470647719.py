N,x=map(int,input().split())
a=[int(i) for i in input().split()]
ans=0
for i in range(N):
    if a[i]>x:
        ans+=a[i]-x
        a[i]=x
for i in range(1,N):
    if a[i-1]+a[i]>x:
        ans+=a[i-1]+a[i]-x
        a[i]=x-a[i-1]
print(ans)
