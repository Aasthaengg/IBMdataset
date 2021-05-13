N,M=map(int,input().split())
MAX=10**5+10
MOD = 10**9 + 7
def COMinit():
    """
    逆元テーブルをつくる前処理
    計算量はO(n)
    1 <= k <= n <= 1e7程度
    p: 素数
    """
    fac = [0]*MAX
    finv = [0]*MAX
    inv = [0]*MAX

    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[0], inv[1] = 1, 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return fac, finv, inv

fac, finv, inv = COMinit()
if abs(N-M)>=2:
    print(0)
elif abs(N-M)==1:
    ans = fac[N]*fac[M]%MOD
    print(ans)
else:
    ans = 2*fac[N]*fac[M]%MOD
    print(ans)