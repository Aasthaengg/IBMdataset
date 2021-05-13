#coding:utf-8
#1_10_B 2015.4.14
import math

a,b,c = list(map(int,input().split()))
S = a * b * math.sin(math.radians(c)) / 2
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c)))
h = S * 2 / a
print('{:.10f}\n{:.10f}\n{:.10f}'.format(S,L,h))