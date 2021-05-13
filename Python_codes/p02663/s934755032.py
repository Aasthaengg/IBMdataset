#!/usr/bin/env pypy3

import math

h1, m1, h2, m2, k = map(int, input().split())

if h2 < h1:
    h2 += 24

if m2 < m1:
    h2 -= 1
    m2 += 60

allMin = (h2 - h1) * 60 + (m2 - m1)

res = allMin - k
if res < 0:
    res = 0

print(res)
