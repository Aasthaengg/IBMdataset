# -*- coding: utf-8 -*-

import sys
import os
import math


dice = list(map(int, input().split()))
q = int(input())

def dice_roll(c):
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
    # Y???????????¢
    elif c == 'R':
        dice[2] = copy[1]
        dice[4] = copy[2]
        dice[3] = copy[4]
        dice[1] = copy[3]

for i in range(q):
    up, front = list(map(int, input().split()))

    # up???????????????
    num = 0
    while dice[0] != up:
        if num % 2 == 0:
            dice_roll('E')
        else:
            dice_roll('N')
        num += 1

    # front???????????????
    while dice[1] != front:
        dice_roll('R')

    print(dice[2])