#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc131_c

def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def f(x, c, d):
    res = x
    res -= x // c 
    res -= x // d 
    res += x // lcm(c, d)
    return res

a, b, c, d = map(int, input().strip().split())
res = f(b, c, d) - f(a-1, c, d)
print(int(res))
