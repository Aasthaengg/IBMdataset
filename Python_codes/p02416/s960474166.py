# -*- coding: utf-8 -*-

import sys
import os


for s in sys.stdin:
    s = s.strip()
    if s == '0':
        break
    else:
        v = 0
        for c in s:
            v += int(c)
        print(v)