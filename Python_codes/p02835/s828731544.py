#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a1,a2,a3 = map(int, input().split())
sum=a1+a2+a3
if sum >= 22:
  print('bust')
else:
  print('win')
