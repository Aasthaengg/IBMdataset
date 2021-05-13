#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    score = list(map(int, sys.stdin.readline().split()))
    ave = sum(score) / len(score)

    s2 = 0
    for v in score:
        s2 += (v-ave) ** 2
    print(round((s2 / len(score)) ** 0.5, 6))

