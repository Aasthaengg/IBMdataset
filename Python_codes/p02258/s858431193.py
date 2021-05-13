#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                                print_function, unicode_literals)
import sys

n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

c = sys.maxsize
ret = -sys.maxsize - 1
for j in range(n):
    ret = max([ret, r[j] - c])
    if(r[j] < c):
        c = r[j]

print(ret)