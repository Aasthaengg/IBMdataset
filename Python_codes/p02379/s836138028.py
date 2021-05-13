# coding: utf-8
import math
x1,y1,x2,y2 = input().split()

X = float(x2) - float(x1)
Y = float(y2) - float(y1)

length = math.sqrt( X**2 + Y**2 )
print(length)