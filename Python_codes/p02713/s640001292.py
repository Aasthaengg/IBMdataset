#!/usr/bin/env python3
import sys
import math
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def gcd(*numbers):
    return reduce(math.gcd, numbers)

def main():
    K = int(input())

    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            for c in range(1, K + 1):
                ans += gcd(a, b, c)
    print(ans)

if __name__ == '__main__':
    main()
