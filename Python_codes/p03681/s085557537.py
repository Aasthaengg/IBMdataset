n,m=map(int,input().split())
if abs(n-m)>1: print(0)
else:
    mod=10**9+7
    def fact(n):
        ans=1
        for i in range(n):
            ans*=(i+1)
            ans%=mod
        return ans

    ans=(fact(n)*fact(m))%mod
    if n==m: print((2*ans)%mod)
    else: print(ans)