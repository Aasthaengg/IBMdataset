# -*- coding: utf-8 -*-

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, raw_input().split())
print gcd(a, b)