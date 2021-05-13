#!/usr/bin/env python3
def main():
    N = int(input())
    H = [int(x) for x in input().split()]

    INF = 10 ** 5 * 10 ** 4
    dp = [INF] * N
    dp[0] = 0
    dp[1] = abs(H[0] - H[1])
    for i in range(2, N):
        dp[i] = min(dp[i],
                    dp[i - 1] + abs(H[i] - H[i - 1]),
                    dp[i - 2] + abs(H[i] - H[i - 2]))
    print(dp[-1])


if __name__ == '__main__':
    main()
