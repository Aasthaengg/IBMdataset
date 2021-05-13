#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    A = set([int(input()) for x in range(M)])

    mod = 10 ** 9 + 7
    dp = [0] * 10 ** 6
    dp[0] = 1
    for i in range(N + 1):
        if i in A:
            continue
        dp[i + 1] += dp[i] % mod
        dp[i + 2] += dp[i] % mod
    print(dp[N] % mod)


if __name__ == '__main__':
    main()
