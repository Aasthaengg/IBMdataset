n, k = map(int, input().split())
MOD = 10**9+7


def com(n, r):
    X = Y = 1
    if r < 0 or n < r:
        return 0
    if n-r < r:
        r = n-r
    for i in range(1, r+1):
        Y = Y*i % MOD
        X = X*(n-i+1) % MOD
    Y = pow(Y, MOD-2, MOD)
    return X*Y % MOD


for i in range(1, k+1):
    ans = com(k-1, i-1)*com(n-k-(i-1)+i, i)
    print(ans % MOD)
