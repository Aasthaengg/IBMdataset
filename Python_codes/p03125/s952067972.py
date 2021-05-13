# coding: utf-8

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ans = B % A == 0
print((A + B) if ans else (B- A))

