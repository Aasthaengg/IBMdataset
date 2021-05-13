#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def main():
    N = int(input())
    result = 0
    for _ in range(N):
        l, r = map(int, input().split())
        result += (r - l) + 1
    print(result)


if __name__ == "__main__":
    main()
