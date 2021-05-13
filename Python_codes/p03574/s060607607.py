#!/usr/bin/env python3
h, w = map(int, input().split())
s = [[0 if i == "." else -9 for i in input()] for _ in range(h)]
d = ((1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1))
for i in range(h):
    for j in range(w):
        if s[i][j] < 0:
            for x, y in d:
                if 0 <= i + x < h and 0 <= j + y < w:
                    s[i + x][j + y] += 1
for i in s:
    print(*["#" if j < 0 else j for j in i], sep="")
