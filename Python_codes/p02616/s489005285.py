n,k=map(int, input().split())
*a,=map(int, input().split())

ans=1
mod=10**9+7

a.sort()
if a[0]>=0:
    for i in range(n-1,n-k-1,-1):
        ans*=a[i]
        ans%=mod
    print(ans)
    exit()
if a[-1]<=0:
    if k%2:
        for i in range(n-1,n-k-1,-1):
            ans*=a[i]
            ans%=mod
    else:
        for i in range(k):
            ans*=a[i]
            ans%=mod
    print(ans)
    exit()
l=0;r=n-1
if k%2:
    ans=a[-1]
    r-=1
    k-=1
while k:
    if a[l]*a[l+1]>a[r]*a[r-1]:
        ans*=a[l]*a[l+1]
        l+=2
    else:
        ans*=a[r]*a[r-1]
        r-=2
    k-=2
    ans%=mod
   
print(ans)
    
    

