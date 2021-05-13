n,*a=map(int,open(0).read().split())
ans=0
for i in range(n):
    if i+1==a[i] and i!=n-1:
        a[i],a[i+1]=a[i+1],a[i]
        ans+=1
    if i+1==a[i] and i==n-1:
        ans+=1
print(ans)