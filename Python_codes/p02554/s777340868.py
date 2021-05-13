N = int(input())
MOD = 10**9 + 7

def pow_mod(a, n, MOD):
    ret = 1
    for i in range(n):
        ret = a * ret % MOD
    return ret

ans = pow_mod(10, N, MOD) - 2*pow_mod(9, N, MOD) + pow_mod(8, N, MOD)
print(ans % MOD)
