#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

S = input()

odd = ('R', 'U', 'D')
even = ('L', 'U', 'D')

for i, s in enumerate(S):
    if not i % 2 and s not in odd:
        print('No')
        sys.exit()
    if i % 2 and s not in even:
        print('No')
        sys.exit()

print('Yes')

