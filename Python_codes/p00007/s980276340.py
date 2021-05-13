import math
n = input()
m = 100
for i in xrange(n):
    m = m * 1.05
    m = math.ceil(m)
print "%i"%(m*1000)