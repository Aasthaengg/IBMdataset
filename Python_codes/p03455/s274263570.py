# coding: utf-8
a, b = map(int, input().split())
c = (a & b) & 1
if c == 1:
  print("Odd")
else:
  print("Even")