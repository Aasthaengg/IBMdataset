# -*- coding: utf-8 -*-

import math

while True:
    n = int(input())

    if n == 0:
        break

    s = list(map(float, input().split()))
    mean = sum(s) / len(s)

    for i in range(len(s)):
        s[i] = (s[i] - mean) * (s[i] - mean)

    variance = sum(s) / len(s)
    stdev = math.sqrt(variance)

    print(stdev)
