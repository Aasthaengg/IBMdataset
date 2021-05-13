import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 998244353


def main():
    N, K, *LR = map(int, read().split())
    interval = [(l, r) for l, r in zip(*[iter(LR)] * 2)]

    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = -1

    for i in range(1, N + 1):
        dp[i] = (dp[i] + dp[i - 1]) % MOD
        for l, r in interval:
            if i + l <= N:
                dp[i + l] += dp[i]
                if i + r + 1 <= N:
                    dp[i + r + 1] -= dp[i]

    print(dp[N])
    return


if __name__ == '__main__':
    main()
