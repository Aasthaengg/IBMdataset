def main():
    n,k = map(int, input().split())
    MOD = 10**9+7
    NMAX = 2*2*10**5

    fact = [0 for i in range(NMAX+5)]
    fact[0] = 1
    invfact = [0 for i in range(NMAX+5)]
    invfact[0] = 1

    for i in range(NMAX):
        fact[i+1] = (fact[i]*(i+1))%(MOD)

    invfact[NMAX] = pow(fact[NMAX], MOD-2, MOD)
    for i in range(NMAX-1,0,-1):
        invfact[i] = (invfact[i+1] * (i+1)) % MOD

    ans = 0
    if k >= n:
        k = n-1
    for i in range(k+1):
        z = fact[n]*invfact[i]%MOD
        z = z*invfact[n-i]%MOD
        h = fact[n-1]*invfact[i]%MOD
        h = h*invfact[n-i-1]%MOD
        ans += z*h%MOD

    print(ans%MOD)

main()