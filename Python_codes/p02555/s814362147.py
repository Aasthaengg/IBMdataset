#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    S = int(input())
    mod = 10**9 + 7
    
    dp = [0] * (S + 4)
    dp[0] = 1
    dp[3] = 1
    for i in range(4, S + 1):
        for k in range(i - 2):
            dp[i] += dp[k]
    
    print(dp[S] % mod)


if __name__ == "__main__":
    main()
