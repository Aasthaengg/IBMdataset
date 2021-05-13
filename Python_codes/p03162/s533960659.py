import sys

input = sys.stdin.readline


def main():
    N = int(input())
    abc = [None] * N
    for i in range(N):
        abc[i] = tuple(map(int, input().split()))

    dp = [[0, 0, 0] for _ in range(N + 1)]
    for i, (a, b, c) in enumerate(abc):
        dp[i + 1][0] = max(dp[i][1], dp[i][2]) + a
        dp[i + 1][1] = max(dp[i][2], dp[i][0]) + b
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + c

    ans = max(dp[-1])
    print(ans)


if __name__ == "__main__":
    main()
