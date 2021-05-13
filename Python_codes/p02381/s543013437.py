import math

n = input()
while n != 0:
    if n == 0:
        break
    tmp = map(float, raw_input().split())
    ave = 0
    for i in xrange(len(tmp)):
        ave += tmp[i] / n
    u = 0
    for i in xrange(n):
        u += (tmp[i] - ave)**2
    print "%.8f" % math.sqrt(u/n)
    n = input()