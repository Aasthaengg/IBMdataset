# -*- coding: utf-8 -*-

import sys
import os
import math


a, b, C = list(map(float, input().split()))
rad = math.radians(C)
S = 1/2 * a * b * math.sin(rad)

L2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)
L = math.sqrt(L2)
around = a + b + L

h = b * math.sin(rad)

print(S)
print(around)
print(h)