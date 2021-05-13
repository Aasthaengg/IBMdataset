# -*- coding: utf-8 -*-
l = input().strip().split()
a = int(l[0])
b = int(l[1])+1
c = int(l[2])
ret = 0
for i in (range(a,b)):
    if(c % i == 0):
        ret = ret + 1

print(ret)