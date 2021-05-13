# -*- coding: utf-8 -*-

#----------
X,t = list(map(int, input().rstrip().split()))
#----------
x_out = t

if X < x_out:
    print(0)
else:
    print(X - x_out)
