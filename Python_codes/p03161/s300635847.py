#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    H = [int(x) for x in input().split()] + [0] * 200

    INF = 10 ** 10
    dp = [INF] * 10 ** 6
    dp[0] = 0
    for i in range(N):
        for k in range(1, K + 1):
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))
    print(dp[N - 1])


if __name__ == '__main__':
    main()
