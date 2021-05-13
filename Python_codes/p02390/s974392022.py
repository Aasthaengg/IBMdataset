x = int(input())

import math

h = math.floor(x/3600)
m = math.floor((x -h*3600)/60)
s = math.floor(x - h*3600 - m*60)
print(h, ':',m , ':', s, sep="")

