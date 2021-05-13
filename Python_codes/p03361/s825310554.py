#!/usr/bin/env python3
import sys
h, w = map(int, input().split())
s = [[c for c in l.strip()] for l in sys.stdin]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if i != 0:
                if s[i - 1][j] == "#":
                    continue
            if j != 0:
                if s[i][j - 1] == "#":
                    continue
            if j != w - 1:
                if s[i][j + 1] == "#":
                    continue
            if i != h - 1:
                if s[i + 1][j] == "#":
                    continue
            print("No")
            sys.exit()
print("Yes")