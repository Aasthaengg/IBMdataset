import sys

input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    C = list(map(int, input().split()))

    INF = 10 ** 18
    dp = [INF] * (N + 1)
    dp[0] = 0
    for c in C:
        for i in range(c, N + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    ans = dp[-1]
    print(ans)


if __name__ == "__main__":
    main()

