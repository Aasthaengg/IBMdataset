#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        d = gcd(a, b)
        m = a * b // d
        print("{} {}".format(d, m))

if __name__ == "__main__": main()