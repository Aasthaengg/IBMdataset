# -*- coding: utf-8 -*-

s = input().split()
n = int(s[0])
m = int(s[1])
d = int(s[2])

if d==0:
    print(1.0*n*(m-1)/n/n)
else:
    print(2.0*(n-d)*(m-1)/n/n)