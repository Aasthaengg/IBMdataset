# coding: utf-8
import math

a,b,C = map(float,input().split())

C_rad = math.pi * C / 180
h = b * math.sin(C_rad)
S = a * h / 2
L = a + b + math.sqrt((a ** 2 + b ** 2 - 2 * a * b * math.cos(C_rad)))

print("{:.6f}".format(S))
print("{:.6f}".format(L))
print("{:.6f}".format(h))