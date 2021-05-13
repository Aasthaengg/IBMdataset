def comb(n,k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk
n,m=map(int,input().split())
if m>n:
    n,m=m,n
N,M=1,1
mod=10**9+7
for i in range(1,n+1):
    N*=i
    N%=mod
for i in range(1,m+1):
    M*=i
    M%=mod
if n>=m+2:
    print(0)
    exit()
if n==m+1:
    ans=1
if n==m:
    ans=2
ans*=N*M
print(ans%mod)