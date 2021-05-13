MOD = 10**9 + 7
def comb(n, k, MOD):
    if n < k or n < 0 or k < 0:
        return 0
    if k == 0:
        return 1
    iinv = [1] * (k + 1)
    ans = n
    for i in range(2, k + 1):
        iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
        ans *= (n + 1 - i) * iinv[i] % MOD
        ans %= MOD
    return ans
N, K = map(int, input().split())
for i in range(1,K+1):
        print((comb(N-K+1,i,MOD)*comb(K-1,K-i,MOD))%MOD)