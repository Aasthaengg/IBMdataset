# /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math



Sn = str(input())
X,Y = map(int, input().split())

xyn = [0]
for c in Sn:
  if c == 'T':
    xyn.append(0)
  else:
    xyn[-1] += 1

Xn = xyn[2::2]
Yn = xyn[1::2]

dp_x = {xyn[0]}
for i in range(len(Xn)):
  dp_xn = {}
  for j in dp_x:
    dp_xn[j+Xn[i]] = 1
    dp_xn[j-Xn[i]] = 1
  dp_x = dp_xn

dp_y = {0}
for i in range(len(Yn)):
  dp_yn = {}
  for j in dp_y:
    dp_yn[j+Yn[i]] = 1
    dp_yn[j-Yn[i]] = 1
  dp_y = dp_yn


if X in dp_x and Y in dp_y:
  print("Yes")
else:
  print("No")
