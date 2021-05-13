# coding:utf-8
import math
array = map(int, raw_input().split())
a = array[0]
b = array[1]
C = array[2]
rad = math.radians(C)
S = a * b * math.sin(rad) / 2.0
L = a + b + math.sqrt(math.pow(a,2) + math.pow(b,2) - 2 * a * b * math.cos(rad))
h = b * math.sin(rad)
print S
print L
print h

