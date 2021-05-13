def main():
    mod = 10**9+7
    k = int(input())
    s = input()
    n = len(s)
    fact = [1, 1]
    for i in range(2, 2*(10**6)+1):
        fact.append(fact[-1]*i % mod)

    def nCr(n, r, mod=10**9+7):
        return pow(fact[n-r]*fact[r] % mod, mod-2, mod)*fact[n] % mod

    ans = 0
    for i in range(k+1):
        ans = (ans+nCr(n+k, i)*pow(25, i, mod)) % mod
    print(ans)


main()
