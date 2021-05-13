# -*- coding: utf-8 -*-

import sys
import os


def chessboard(w, h):
    even_row = ('#.' * 150)[:w]
    odd_row = ('.#' * 150)[:w]
    for i in range(h):
        if i % 2 == 0:
            print(even_row)
        else:
            print(odd_row)

for s in sys.stdin:
    H, W = list(map(int, s.split()))
    if W == H == 0:
        break
    else:
        chessboard(W, H)
        print()