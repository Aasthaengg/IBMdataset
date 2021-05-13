from sys import stdin
import sys, math

a, b, h, m = [int(x) for x in stdin.readline().rstrip().split()]

x = 30*h + 0.5*m
y = 6*m

z = abs(x-y)
if z > 180: z = 360 - z

c = a**2 + b**2 - 2*a*b*math.cos(math.radians(z))
c = math.sqrt(c)

print(c)