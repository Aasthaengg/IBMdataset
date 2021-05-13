#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

S = input()

l, r = 0, len(S)-1
count = 0
while l < r:
    if S[l] != S[r]:
        count += 1
    l += 1
    r -= 1

print(count)
