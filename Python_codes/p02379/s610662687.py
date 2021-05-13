import sys
import math

def distance(x1, y1, x2, y2):
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)	

#fin = open("test.txt", "r")
fin = sys.stdin

[x1, y1, x2, y2] = list(map(float, fin.readline().split()))

print("{0:.5f}".format(distance(x1, y1, x2, y2)))