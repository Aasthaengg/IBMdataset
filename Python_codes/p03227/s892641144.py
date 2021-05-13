# /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math



s = str(input())

if len(s) == 2:
  print(s)
else:
  print(s[::-1])