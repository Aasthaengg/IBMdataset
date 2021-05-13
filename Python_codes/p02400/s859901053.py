import sys

PI = 3.141592653589793

r = float(sys.stdin.readline().strip())
area = r * r * PI
periphery = r * 2 * PI

print('%.6f %.6f' % (area, periphery))