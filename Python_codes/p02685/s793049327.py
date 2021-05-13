import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def binom_preprocess(n, MOD=998244353):
    f = [0 for i in range(n+1)]  # n!
    invf = [0 for i in range(n+1)]  # (n!)^-1
    f[0] = 1
    f[1] = 1
    invf[0] = 1
    invf[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] * i % MOD
        invf[i] = pow(f[i], MOD-2, MOD)
    return f, invf


def binom(n, k, f, invf, MOD=998244353):
    if n < k or n < 0 or k < 0:
        return 0
    else:
        return (f[n] * invf[k] % MOD) * invf[n-k] % MOD


def read():
    N, M, K = map(int, input().strip().split())
    return N, M, K


# 998244353は素数
def solve(N, M, K, MOD=998244353):
    ans = 0
    f, invf = binom_preprocess(N)
    for k in range(K+1):
        ans += binom(N-1, N-k-1, f, invf) * M * pow(M-1, N-k-1, MOD)
        ans %= MOD
    return ans


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
