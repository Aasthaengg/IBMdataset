# -*- coding:utf-8 -*-
a,b = map(int,input().split())

if a !=b:
    if a<b:
        print("a < b")
    else:
        print("a > b")
else:
    print("a == b")