n,m = map(int,input().split())
mod = 10**9+7

if abs(n-m)>1:
    print(0)
else:
    ans=1
    for i in range(1,n+1):
        ans=ans*i%mod
    for j in range(1,m+1):
        ans=ans*j%mod
    if n==m:
        ans=ans*2%mod
    print(ans)