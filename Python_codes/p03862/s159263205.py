n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n-1):
    if a[i]+a[i+1]>x:
        d=a[i+1]+a[i]-x
        if d<=a[i+1]:
            ans+=d
            a[i+1]-=d
        else:
            ans+=a[i+1]
            a[i+1]=0
            d=a[i]-x
            ans+=d
            a[i]-=d
print(ans)

