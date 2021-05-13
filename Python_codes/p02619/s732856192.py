# -*- coding: utf-8 -*-
import time
import numpy as np

start = time.time()
limit_time = 1.8

# 整数の入力
d = int(input())
c = [int(i) for i in input().split()]
s = [[int(i) for i in input().split()] for j in range(d)]

def point(t):
    result = 0
    map = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
        10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0,
        20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0
    }
    for i in range(d):
        comp = t[i] - 1
        day = i + 1
        map[comp] = day
        result = result + s[i][comp]
        for cc in range(26):
            result = result - c[cc] * (day - map[cc])
        print(result)
    return result

t = [int(input()) for i in range(d)]

point(t)