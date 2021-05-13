import sys

input = sys.stdin.readline


def main():
    N = int(input())
    abc = [0] * N
    for i in range(N):
        abc[i] = list(map(int, input().split()))

    dp = [[0] * 3 for _ in range(N)]
    dp[0] = abc[0]
    for i, (a, b, c) in enumerate(abc[1:], start=1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c

    ans = max(dp[-1])
    print(ans)


if __name__ == "__main__":
    main()
