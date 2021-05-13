#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter


def main():

    N = int(input())
    A = list(map(int, input().split()))
    arr = [abs(i - (N - i - 1)) for i in range(N)]
    result = 0
    mod = 10**9 + 7

    if Counter(A) == Counter(arr):
        result = (2**(N // 2)) % mod

    print(result)


if __name__ == "__main__":
    main()
