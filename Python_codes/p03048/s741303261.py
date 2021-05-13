#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
# input = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a, b, c, n = map(int, input().split())
ans = 0
for i in range(3001):
    for j in range(3001):
        if n >= i * a + j * b and (n - i * a - j * b) % c == 0:
            ans += 1
print(ans)
