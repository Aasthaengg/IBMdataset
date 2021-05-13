n,t=map(int,input().split())
ans=0
a=list(map(int,input().split()))
if n==1:
    print(t)
else:
    for i in range(1,n):
        if a[i]-a[i-1]>t:
            ans+=t
        else:
            ans+=a[i]-a[i-1]
        if i==n-1:
            ans+=t
    print(ans)
