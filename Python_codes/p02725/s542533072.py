k,n=map(int,input().split())
a=list(map(int,input().split()))

ans=1e9
for i in range(n):
    if i==0:
        ans=min(ans,a[n-1]-a[0])
    else:
        ans=min(ans,k-a[i]+a[i-1])

print(ans)