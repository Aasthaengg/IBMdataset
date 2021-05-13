#!/usr/bin/env python
# -*- coding: utf-8 -*-


def maxprofit(n, rs):
    maxp = rs[1] - rs[0]
    minp = rs[0]
    for i in range(1, n):
        maxp = max(maxp, rs[i] - minp)
        minp = min(minp, rs[i])
    return maxp


def main():
    n = int(input())
    rs = [int(input()) for i in range(n)]
    print(maxprofit(n, rs))

if __name__ == "__main__":
    main()