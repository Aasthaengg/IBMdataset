# -*- coding: utf-8 -*-

import sys

for line in sys.stdin.readlines():
    x, y = line.strip().split()

    if x == "0" and y == "0":
        break

    if int(x) < int(y):
        print("{} {}".format(x, y))
    else:
        print("{} {}".format(y, x))