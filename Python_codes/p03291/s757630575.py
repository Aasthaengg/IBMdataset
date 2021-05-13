#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

MOD = 10**9+7

def main():
    s = input()
    dp = [[0 for _ in range(4)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i, c in enumerate(s):
        if c == '?':
            for j in range(4):
                dp[i+1][j] = 3*dp[i][j]
        else:
            for j in range(4):
                dp[i+1][j] = dp[i][j]
        if c == 'A' or c == '?':
            dp[i+1][1] += dp[i][0]
        if c == 'B' or c == '?':
            dp[i+1][2] += dp[i][1]
        if c == 'C' or c == '?':
            dp[i+1][3] += dp[i][2]
        if i & 1:
            for j in range(4):
                dp[i+1][j] %= MOD

    print(dp[len(s)][3]%MOD)


if __name__ == '__main__':
    main()
