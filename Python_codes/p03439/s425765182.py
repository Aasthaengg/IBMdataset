#!/usr/bin/env python3
import sys

def query(i, memo={}):
    if i in memo:
        return memo[i]
    print(i)
    sys.stdout.flush()
    s = input()
    if s == 'Male':
        memo[i] = 0
    elif s == 'Female':
        memo[i] = 1
    else:
        sys.exit()
    return memo[i]

n = int(input())
l, r = -1, n
while True:
    m = (l + r) // 2
    if query(0) ^ query(m) == m & 1:
        l = m
    else:
        r = m
