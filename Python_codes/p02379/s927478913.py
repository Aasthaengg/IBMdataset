import math
x = map(float, (raw_input()).split(" "))

print math.sqrt((x[2]-x[0])*(x[2]-x[0]) + (x[3]-x[1])*(x[3]-x[1]))