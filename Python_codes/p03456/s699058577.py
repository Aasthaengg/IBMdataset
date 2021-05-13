#-*- coding: utf-8 -*-
a, b = map(int, input().split())
if int(str(a)+str(b))**0.5%1==0:
    print("Yes")
if int(str(a)+str(b))**0.5%1!=0:
    print("No")