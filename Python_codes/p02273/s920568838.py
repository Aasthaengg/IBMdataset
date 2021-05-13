from enum import Enum
from queue import Queue
import collections

import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def kock(n,p1x,p1y,p2x,p2y):
    if n == 0:
        return

    sx = (2 * p1x + 1 * p2x) / 3
    sy = (2 * p1y + 1 * p2y) / 3
    tx = (1 * p1x + 2 * p2x) / 3
    ty = (1 * p1y + 2 * p2y) / 3
    ux = (tx - sx)*math.cos(math.pi/3) - (ty - sy)*math.sin(math.pi/3) + sx
    uy = (tx - sx)*math.sin(math.pi/3) + (ty - sy)*math.cos(math.pi/3) + sy

    kock(n-1,p1x,p1y,sx,sy)
    print("%f %f"%(sx,sy))
    kock(n-1,sx,sy,ux,uy)
    print("%f %f"%(ux,uy))
    kock(n-1,ux,uy,tx,ty)
    print("%f %f"%(tx,ty))
    kock(n-1,tx,ty,p2x,p2y)
#    print("%f %f"%(p2x,p2y))

n = int(input())
p1x = 0; p1y = 0; p2x = 100; p2y = 0
print("%f %f"%(p1x,p1y))
kock(n,p1x,p1y,p2x,p2y)
print("%f %f"%(p2x,p2y))

