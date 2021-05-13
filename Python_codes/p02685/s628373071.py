N,M,K=list(map(int,input().split()))

mod=998244353

com=1
ans=0

for i in range(K+1):
    ans+=M*com*pow(M-1,N-1-i,mod)
    ans%=mod
    com*=(N-1-i)*pow(i+1,mod-2,mod)
    com%=mod

print(ans)