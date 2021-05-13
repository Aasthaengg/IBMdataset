#!/usr/bin/env python3

import sys


if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

N = int(input())
S = input()
T = ""
for ch in S:
    T += chr(ord('A') + (ord(ch) - ord('A') + N) % 26)
print(T)
