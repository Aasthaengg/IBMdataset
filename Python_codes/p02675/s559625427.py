#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
hon = [2,4,5,7,9]
pon = [0,1,6,8]
#bon = [3]
r=n%10
if r in hon:
  print('hon')
elif r in pon:
  print('pon')
else:
  print('bon')
