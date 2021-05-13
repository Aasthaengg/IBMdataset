import math
a,b,c = map(float,raw_input().split())
print "%.8f" %float(a*b*math.sin(math.radians(c))/2)
print "%.8f" %float(a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(c))))
print "%.8f" %float(b*math.sin(math.radians(c)))