import sys

N_MAX = 200000 + 5
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7

# ## COMBINATION (MOD) ## #

fac = [1, 1]  # 元テーブル
facinv = [1, 1]  # 逆元テーブル
inv = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N_MAX + 1):
    fac.append((fac[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)


def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    # r = min(r, n-r)
    return fac[n] * facinv[r] * facinv[n - r] % MOD


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    k = min(n, k)

    ans = 0
    for m in range(k+1):
        empty = cmb(n, m)
        member = cmb(n - 1, n - m - 1)
        ans += (empty * member) % MOD
        ans %= MOD

    print(ans)


main()
