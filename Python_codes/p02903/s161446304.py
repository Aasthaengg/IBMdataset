#!/usr/bin/env python3
import sys
input = sys.stdin.readline

h, w, a, b = map(int, input().split())
if a > w // 2 or b > h // 2:
    print("No")
    exit()
ans = [[0] * w for _ in range(h)]
for i in range(0, b):
    for j in range(0, a):
        ans[i][j] = 1
for i in range(b, h):
    for j in range(a, w):
        ans[i][j] = 1
for line in ans:
    print("".join([str(item) for item in line]))