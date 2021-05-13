# -*- coding: utf-8 -*-

import math

while True:
    n = int(raw_input())
    if n == 0:
        break
    else:
        scores = map(int, raw_input().split())

        ave = 0.0
        for i in scores:
            ave += i
        ave /= n

        dev = 0.0
        for i in scores:
            dev += (i-ave)*(i-ave)
        dev /= n

        print math.sqrt(dev)