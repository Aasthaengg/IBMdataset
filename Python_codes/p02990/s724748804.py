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
n,k=map(int,input().split())
MOD=10**9+7
print(n-k+1)
if n==1:
    exit()
for i in range(2,k+1):
    ans=comb(n-k+1,i)*comb(k-1,i-1)
    print(ans%MOD)