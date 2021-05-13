# -*- coding: utf-8 -*-
a,b = map(int, input().split(" "))

d = int(a/b)
r = a%b
f = float(a)/b

print("{} {} {:.6f}".format(d,r,f))