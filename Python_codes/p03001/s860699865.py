#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc130_c

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

w, h, x, y = map(int, input().strip().split())
area = w * h / 2
has_points = 0
if 2 * x == w and 2 * y == h:
    has_points = 1
# if abs(2*x-w) == 0 and h > 1:
#     has_points = 1
# elif abs(2*y-h) == 0 and w > 1:
#     has_points = 1
# elif w >= 3*abs(2*x-w) and h >= 3*abs(2*y-h):
#     has_points = 1
# elif gcd(abs(2*x-w), abs(2*y-h)) > 1:
#     has_points = 1

print(area, has_points)
