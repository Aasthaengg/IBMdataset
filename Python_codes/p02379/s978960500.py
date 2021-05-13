import math
import sys

x1, y1, x2, y2 = [float(x) for x in sys.stdin.readline().split()]
print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))