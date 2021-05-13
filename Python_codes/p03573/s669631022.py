# -*- coding: utf-8 -*-
d = list(map(int, input().split()))
d.sort()
if(d[0] == d[1]):
  print(d[2])
else:
  print(d[0])
