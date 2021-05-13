# -*- coding: utf-8 -*-
A,B,C = [int(i) for i in input().split()]

X = A + B
if C <= X:
    print("Yes")
else:
    print("No")
