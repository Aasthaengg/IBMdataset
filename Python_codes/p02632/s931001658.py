mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    # comb init
    # mod = 1000000007
    nmax = 2 * 10 ** 6 + 10  # change here
    fac = [0] * nmax
    finv = [0] * nmax
    inv = [0] * nmax
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, nmax):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

    def comb(n, r):
        if n < r:
            return 0
        else:
            return (fac[n] * ((finv[r] * finv[n - r]) % mod)) % mod

    K = int(input())
    S = input().rstrip('\n')
    N = len(S)

    ans = 0
    for k in range(K+1):
        ans = (ans + (pow(25, K-k, mod) * comb(N+K, N+k))%mod)%mod
    print(ans)



if __name__ == '__main__':
    main()
