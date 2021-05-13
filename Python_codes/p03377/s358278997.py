# -*- coding: utf-8 -*-

A,B,X = [int(i) for i in input().rstrip().split()]

if (X>=A) and (X-A)<=B:
    print("YES")
else:
    print("NO")
