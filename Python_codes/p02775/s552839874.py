#!/usr/bin/env python3

import sys
import math
import itertools

def main():
    ns = list(map(int, sys.stdin.readline().strip()))
    ns.reverse()
    ns.append(0)

    ans = 0
    lastpay = 0

    for i in range(len(ns)):
        if lastpay == 0:
            if ns[i] <= 4 or (ns[i] == 5 and ns[i + 1] <= 4):
                ans += ns[i]
                lastpay = 0
            else:
                ans += 1 + (10 - ns[i])
                lastpay = 1
        else:
            if lastpay + ns[i] <= 4 or (lastpay + ns[i] == 5 and ns[i + 1] <= 4):
                ans += ns[i]
                lastpay = 0
            else:
                ans += 1 - 1 + (9 - ns[i])
                lastpay = 1
    print(ans)

if __name__ == '__main__':
    main()