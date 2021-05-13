import math
p = raw_input().split()
x = math.fabs(float(p[0]) - float(p[2]))
y = math.fabs(float(p[1]) - float(p[3]))
print '%.8f' % math.sqrt(x**2 + y**2)