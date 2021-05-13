# -*- coding: utf-8 -*-

a,b,c = map(int, input().split())

if c >= a:
    if c <= b:
        print("Yes")
    else:
        print("No")
else:
    print("No")