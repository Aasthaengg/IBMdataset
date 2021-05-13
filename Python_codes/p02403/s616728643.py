# -*- coding: utf-8 -*-

import sys
import os


def rect(w, h):
    row = '#' * w + '\n'
    print(row * h)

for s in sys.stdin:
    H, W = list(map(int, s.split()))
    if W == H == 0:
        break
    else:
        rect(W, H)