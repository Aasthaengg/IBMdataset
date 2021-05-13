#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?????¢
"""
import math
x1, y1, x2, y2 = map(float,input().strip().split())
x = x1 - x2
y = y1 - y2

distance = math.sqrt(x * x + y * y)

print(distance)