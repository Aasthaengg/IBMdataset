import math

I = (raw_input()).split(" ")
a = int(I[0])*1.0
b = int(I[1])*1.0
C = (int(I[2])*math.pi)/180

print (1.0/2)*a*b*math.sin(C)
print math.sqrt(a*a + b*b - 2*a*b*math.cos(C)) + a + b
print b*math.sin(C)