#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    x, mod = 1, 10**9 + 7
    for i in range(1, N + 1):
        x *= i
    result = 1

    for i in range(2, N + 1):
        cnt = 1
        while x % i == 0:
            x = x // i
            cnt += 1
        result *= cnt

    result = result % mod
    print(result)


if __name__ == "__main__":
    main()
