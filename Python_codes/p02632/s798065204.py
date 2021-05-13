import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())
    S = readline().strip()

    COM_MAX = 2 * 10 ** 6

    fac, finv, inv = [0] * (COM_MAX + 1), [0] * (COM_MAX + 1), [0] * (COM_MAX + 1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2, COM_MAX + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def mod_com(n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD

    N = len(S)
    L = K + N

    ans = 0
    p25 = pow(25, K, MOD)
    inv25 = pow(25, MOD - 2, MOD)
    p26 = 1
    for i in range(K + 1):
        ans = (ans + mod_com(L - i - 1, N - 1) * p25 * p26) % MOD
        p25 = p25 * inv25 % MOD
        p26 = p26 * 26 % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
