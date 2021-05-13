#!/usr/bin/env python3
def main():
    N = int(input())
    happiness = [list(map(int, input().split())) for _ in range(N)]

    dp = [0, 0, 0]
    for a, b, c in happiness:
        dp = [max(dp[1], dp[2]) + a,
              max(dp[0], dp[2]) + b,
              max(dp[0], dp[1]) + c]
    print(max(dp))


if __name__ == '__main__':
    main()
