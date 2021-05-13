#!/usr/bin/env python3

#import
#import math
#import numpy as np
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):

        if A[i][j] != "#":
            continue

        ul = 0
        dr = 0

        if i != 0:
            if A[i - 1][j] == "#":
                ul += 1
        if i != H - 1:
            if A[i + 1][j] == "#":
                dr += 1
        if j != 0:
            if A[i][j - 1] == "#":
                ul += 1
        if j != W - 1:
            if A[i][j + 1] == "#":
                dr += 1

        if dr > 1 or ul > 1:
            print("Impossible")
            exit()

print("Possible")
