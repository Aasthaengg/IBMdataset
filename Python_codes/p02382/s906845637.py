import math

n = input()

dis_1 = 0.0
dis_2 = 0.0
dis_3 = 0.0
dis_inf = 0.0

x = map(float, raw_input().split())
y = map(float, raw_input().split())

for i in xrange(n):
    dis_1 += abs(x[i] - y[i])
print "%.6f" % dis_1

for i in xrange(n):
    dis_2 += (x[i] - y[i])**2
print "%.6f" % math.sqrt(dis_2)

for i in xrange(n):
    dis_3 += abs(x[i] - y[i])**3
print "%.6f" % math.pow(dis_3, (1.0/3.0))

max_num = 0
for i in xrange(n):
    max_num = max(max_num, abs(x[i] - y[i]))
dis_inf = max_num
print "%.6f" % dis_inf