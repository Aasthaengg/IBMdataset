#!/usr/bin/env python3
import sys


input = sys.stdin.readline
def IS(cb): return cb(input().strip())
def IL(cb): return [cb(s) for s in input().strip().split()]
def IR(cb, rows): return [IS(cb) for _ in range(rows)]
def ILL(cb, rows): return [IL(cb) for _ in range(rows)]


def solve():
    X, Y = IL(int)
    ans = 1
    while Y // 2 >= X:
        ans += 1
        Y //= 2
    print(ans)

solve()
