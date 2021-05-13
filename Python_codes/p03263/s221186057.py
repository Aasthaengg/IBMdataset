#!/usr/bin/env python3
import sys
input = sys.stdin.readline
from collections import Counter

h, w = map(int, input().split())
field = []
ans = []
for hgt in range(h):
    line = [int(item) for item in input().split()]
    ret = []
    for i in range(1, w):
        if line[i-1] % 2 == 1:
            line[i-1] -= 1
            line[i] += 1
            ans.append((hgt+1, i, hgt+1, i+1))
    field.append(line)

for i in range(1, h):
    if field[i-1][w-1] % 2 == 1:
        field[i-1][w-1] -= 1
        field[i][w-1] += 1
        ans.append((i, w, i+1, w))

print(len(ans))
for line in ans:
    print(*line)