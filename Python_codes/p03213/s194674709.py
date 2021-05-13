# https://atcoder.jp/contests/abc114/tasks/abc114_d
# https://betrue12.hateblo.jp/entry/2018/12/02/224027
# https://coonevo.hatenablog.com/entry/2020/03/18/192431

from collections import defaultdict

MAX_N = 101

def solve():
    n = int(input())
    # dp[i][j]: i番目までの素因数で約数をj個持つ数の個数
    # 2 ~ n までの素因数分解 (これがn!の素因数分解)
    e = [0] * (n + 1)
    for i in range(2, n + 1):
        cur = i
        for j in range(2, i + 1):
            while cur % j == 0:
                e[j] += 1
                cur //= j

    primes = []
    for i in range(n + 1):
        if e[i] > 0:
            primes.append(i)

    dp = [[0] * MAX_N for _ in range(MAX_N)]
    dp[0][1] = 1
    for i in range(len(primes)):
        for j in range(MAX_N):
            for cnt in range(e[primes[i]] + 1):
                dp[i + 1][min(100, j * (cnt + 1))] += dp[i][j]
    print(dp[len(primes)][75])

if __name__ == '__main__':
    solve()