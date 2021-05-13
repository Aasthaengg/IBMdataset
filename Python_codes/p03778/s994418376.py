# -*- coding: utf-8 -*-

W,a,b = list(map(int, input().rstrip().split()))
#-----
d = abs(a-b) - W
if d >= 0:
  print(d)
else:
  print("0")
