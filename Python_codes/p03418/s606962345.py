n,k=map(int,input().split())
ans=0
if k==0:
    print(n**2)
else:
    for i in range(k+1,n+1):
        temp=(i-k)*(n//i)
        r=n%i
        if r>=k:
            temp=temp+(r+1-k)
        ans=ans+temp
    print(ans)
