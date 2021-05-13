#!/usr/bin/env python3


mod = 10 ** 9 + 7


def main():
    n = int(input())

    dp = [0 for i in range(n + 1)]

    if n == 1 or n == 2:
        print(0)
        return
    elif n in (3, 4, 5):
        print(1)
        return

    dp[3] = 1
    dp[4] = 1
    dp[5] = 1
    dp[6] = 2
    for i in range(7, n + 1):
        dp[i] += 1
        for j in range(3, i - 2):
            dp[i] += dp[j] % mod

    print(dp[n] % mod)


main()

