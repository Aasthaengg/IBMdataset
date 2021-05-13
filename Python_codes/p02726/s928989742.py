#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n, x, y = [int(x) for x in input().split()]
ans = [0 for k in range(n)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ans[min(abs(i - j), abs(x - i) + 1 + abs(y - j), abs(y - i) + 1 + abs(x - j))] += 1
print(*(ans[1:]), sep='\n')
