# coding: utf-8
# Your code here!

import math
x1, y1, x2, y2 = map(float, input().split())
result = math.sqrt( (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1) )
print(result)
