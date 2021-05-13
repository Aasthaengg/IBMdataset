# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:09:47 2020

@author: sd18016
"""   

x = int(input())

if x <= 6:
    print("1")
elif x <= 11:
    print("2")
else:
    a = x // 11
    b = x % 11
    if b == 0:
        print(2*a)
    elif b > 6:
        print(2*a+2)
    else:
        print(2*a+1)

