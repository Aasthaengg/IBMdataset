import math

r = float(input())
area = r*r*math.pi
length = 2*math.pi*r

print("{:8f} {:8f}".format(area,length))