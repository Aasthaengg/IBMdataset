#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??´?????????
"""
inp = input().strip().split(" ")
row = int(inp[0])
col = int(inp[1])

cells = [[0 for r in range(col+1)] for c in range(row+1)]
for r in range(row):
    inp = input().strip().split(" ")
    for c in range(col):
        cells[r][c] = int(inp[c])
        cells[row][c] += cells[r][c]
        cells[r][col] += cells[r][c]
    cells[row][col] += cells[r][col]

for r in range(row+1):
    print(" ".join(map(str,cells[r])))