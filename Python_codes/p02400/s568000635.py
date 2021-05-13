from math import pi

r = float(input())

s = "{:.6f}".format(r ** 2 * pi) 
l = "{:.6f}".format(r * 2 * pi)

print(s, l)