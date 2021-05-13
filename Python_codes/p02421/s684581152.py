#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
t_score = h_score = 0

for i in range(n):
    t_card, h_card = sys.stdin.readline().split()
    if t_card > h_card:
        t_score += 3
    elif t_card < h_card:
        h_score += 3
    else:
        t_score += 1
        h_score += 1

print(t_score, h_score)

