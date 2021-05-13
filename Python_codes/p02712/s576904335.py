#!/usr/bin/env python3
n = int(input())


def e(k):
    m = n // k
    print
    return (m + 1) * m // 2 * k


print(e(1) - e(3) - e(5) + e(15))
