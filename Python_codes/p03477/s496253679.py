#!/usr/bin/env python3
import sys


input = sys.stdin.readline
def IS(cb): return cb(input().strip())
def IL(cb): return [cb(s) for s in input().strip().split()]
def IR(cb, rows): return [IS(cb) for _ in range(rows)]
def ILL(cb, rows): return [IL(cb) for _ in range(rows)]


def solve():
    A, B, C, D = IL(int)
    if A + B > C + D:
        print('Left')
    elif A + B == C + D:
        print('Balanced')
    else:
        print('Right')


solve()
