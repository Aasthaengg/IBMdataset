#!/usr/bin/env python3
# coding=utf-8

import sys

n = int(sys.stdin.readline().strip())

txy = [(0,0,0)]+[tuple(map(int, l.strip().split(" "))) for l in sys.stdin.readlines()]
check_txy = [abs(_x - _xp) + abs(_y - _yp) <= _t - _tp and (_t + _x + _y) % 2 == 0 for (_t, _x, _y), (_tp, _xp, _yp) in zip(txy[1:], txy)]
if all(check_txy):
    print("Yes")
else:
    print("No")
