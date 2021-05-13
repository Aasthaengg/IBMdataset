#!/usr/bin/python
# -*- Coding: utf-8 -*-

x, y = input().split()

a = int(x, 16)
b = int(y, 16)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")