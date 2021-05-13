#!/usr/bin/env python3
n, *g = [i.split() for i in open(0)]
h, w = map(int, n)
d = ((1, 0), (-1, 0), (0, -1), (0, 1))
for i in range(h):
    for j in range(w):
        if g[i][0][j] == "#":
            if all(g[i + p][0][j + q] == "." for p, q in d
                   if 0 <= i + p < h and 0 <= j + q < w):
                print("No")
                exit()
print("Yes")
