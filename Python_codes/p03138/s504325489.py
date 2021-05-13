n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[0]*42
for i in range(n):
    p=l[i]
    j=0
    while p>0:
        a[j]+=p%2
        p=p//2
        j+=1
ans=0
for i in range(41,-1,-1):
    if a[i]<n-a[i]:
        if k>=2**i:
            k-=2**i
            ans+=(2**i)*(n-a[i])
        else:
            ans+=(2**i)*a[i]
    else:
        ans+=(2**i)*a[i]
print(ans)
