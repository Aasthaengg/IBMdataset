#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://qiita.com/e869120/items/eb50fdaece12be418faa
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja


def main():
    n = int(input().strip())
    print(fib(n))


def fib(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    main()

