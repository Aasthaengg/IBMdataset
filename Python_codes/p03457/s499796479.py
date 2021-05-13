# -*- coding: utf-8 -*-
import math

lastT, lastX, lastY = 0, 0, 0
flag = "Yes"

N = int(input())
for i in range(N):
    t, x, y = map(int, input().split())

    # print( math.fabs(t - lastT) + math.fabs(t - lastT) )

    if ( t - lastT < math.fabs(x - lastX) + math.fabs(y - lastY)
        or ( (t - lastT) - math.fabs(x - lastX) - math.fabs(y - lastY) ) % 2 == 1 ):
        flag = "No"

    lastT = t
    lastX = x
    lastY = y

print(flag)
