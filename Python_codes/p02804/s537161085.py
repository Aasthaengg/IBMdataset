n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
mod=10**9+7
fact=[1]*(n+1)
inv=[1]*(n+1)
for i in range(2,n+1):
    fact[i]=i*fact[i-1]%mod
inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(n,1,-1):
    inv[i-1]=inv[i]*i%mod
ans=0
for i in range(n):
    if i>=k-1:
        ans+=l[i]*fact[i]*inv[k-1]*inv[i-k+1]%mod
    if n-i-1>=k-1:
        ans-=l[i]*fact[n-i-1]*inv[k-1]*inv[n-i-1-k+1]%mod
    ans%=mod
print(ans)