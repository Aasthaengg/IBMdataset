#! /usr/bin/env python
# -*- coding: utf-8 -*-

w, h, x, y, r = map(int, raw_input().split())
if -100 <= x <= 100 and -100 <= y <= 100 and \
   0 < w <= 100 and 0 < h <= 100 and 0 < r <= 100:
    if x + r <= w and y + r <= h and x - r >= 0 and y - r >= 0:
        print("Yes")
    else:
        print("No")