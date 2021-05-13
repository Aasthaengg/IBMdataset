#!/usr/bin/python
# coding: UTF-8

a, b, c = map(int,input().split())

if a * b == 0:
  print(0)
elif a + b >= c:
  print(b + c)
else:
  print(a + b * 2 + 1)