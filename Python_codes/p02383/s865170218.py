# -*- coding: utf-8 -*-

import sys
import os
import math


dice = list(map(int, input().split()))
orders = input().strip()
for c in orders:
    copy = dice[:]
    if c == 'E':
        dice[2] = copy[0]
        dice[5] = copy[2]
        dice[3] = copy[5]
        dice[0] = copy[3]
    elif c == 'N':
        dice[0] = copy[1]
        dice[4] = copy[0]
        dice[5] = copy[4]
        dice[1] = copy[5]
        pass
    elif c == 'S':
        dice[1] = copy[0]
        dice[0] = copy[4]
        dice[4] = copy[5]
        dice[5] = copy[1]
    elif c == 'W':
        dice[0] = copy[2]
        dice[2] = copy[5]
        dice[5] = copy[3]
        dice[3] = copy[0]
print(dice[0])