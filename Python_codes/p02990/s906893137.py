n, k = map(int,input().split())


MOD=10**9+7
def comb(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    k = min(n-k,k)
    ans = 1
    inv = [1]*(k+1)
    if k >= 1:
        ans *= (n-k+1)%MOD
    for i in range(2,k+1):
        inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
        ans = ans*(n-k+i)*inv[i]%MOD
    return ans


for i in range(1, k+1):
    ans_i = comb(n-k+1, i) * comb(k-1, i-1)
    print(ans_i % MOD)
