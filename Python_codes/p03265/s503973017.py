import numpy as np
import sys

input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())

yl = (y2 -y1)
xl = (x2 -x1)

print(x2-yl,y2+xl,x1-yl,y1+xl)
