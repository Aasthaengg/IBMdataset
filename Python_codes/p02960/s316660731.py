import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    S = S[::-1]

    dp = [0] * 13
    dp[0] = 1
    p = 1

    for c in S:
        dp, dp_prev = [0] * 13, dp
        for k in range(13):
            if c == '?':
                for j in range(10):
                    dp[(p * j + k) % 13] = (dp[(p * j + k) % 13] + dp_prev[k]) % MOD
            else:
                dp[(p * int(c) + k) % 13] = (dp[(p * int(c) + k) % 13] + dp_prev[k]) % MOD

        p = p * 10 % 13

    print(dp[5])
    return


if __name__ == '__main__':
    main()
