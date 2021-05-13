n=int(input())
if n==2:
    print(0)
    exit()
ans=n-1
for i in range(int(n**0.5)+1,2,-1):
    # print(n//i+1)
    l,r=n//i+1,n//(i-1)+1
    while l+1<r:
        mid=(l+r)//2
        if n//mid<=n%mid:
            l=mid
        else:
            r=mid
    if n//l==n%l:
        ans+=l
print(ans)
