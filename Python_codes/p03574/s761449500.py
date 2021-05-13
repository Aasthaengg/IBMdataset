#!/usr/bin/env python3
import sys
h, w = map(int, input().split())
s = [[c for c in l.strip()] for l in sys.stdin]



for i in range(h):
    line = ""
    for j in range(w):
        
        cnt = 0

        if s[i][j] == "#":
            line += "#"
        else:
            #上の行3マス
            if i != 0:
                if j != 0:
                    if s[i - 1][j - 1] == "#":
                        cnt += 1
                if s[i - 1][j] == "#":
                    cnt += 1
                if j != w - 1:
                    if s[i - 1][j + 1] == "#":
                        cnt += 1

            #同じ行2マス
            if j != 0:
                if s[i][j - 1] == "#":
                    cnt += 1
            if j != w - 1:
                if s[i][j + 1] == "#":
                    cnt += 1

            #下の行3マス
            if i != h - 1:
                if j != 0:
                    if s[i + 1][j - 1] == "#":
                        cnt += 1
                if s[i + 1][j] == "#":
                    cnt += 1
                if j != w - 1:
                    if s[i + 1][j + 1] == "#":
                        cnt += 1
            line += str(cnt)
    print(line)