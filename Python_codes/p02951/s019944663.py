#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int, input().split())
r=a-b
if r >= c:
  print(0)
else:
  print(c-r)
