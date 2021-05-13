import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))
    s = list(map(int, readline().split()))
    t = list(map(int, readline().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i, val_s in enumerate(s, 1):
        for j, val_t in enumerate(t, 1):
            num = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            if val_s == val_t:
                num += dp[i - 1][j - 1] + 1
            num %= MOD
            dp[i][j] = num

    print(dp[n][m] + 1)


if __name__ == '__main__':
    main()
