MOD=10**9+7
N=int(input())
ans=pow(10,N,MOD)
ans-=2*pow(9,N,MOD)
ans+=pow(8,N,MOD)
ans%=MOD
print(ans)