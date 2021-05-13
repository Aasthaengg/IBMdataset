#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    P = list(int(input()) for _ in range(N))
    dp = [0]*(N+1)   #dp[i]:１づつ増加する部分列の最大の数字がiとなるものの最大長さ

    ret = 0;
    for p in P:
        dp[p] = dp[p - 1] + 1
        ret = max(ret, dp[p])

    print(N - ret)

if __name__ == '__main__':
    main()