# -*- coding: utf-8 -*-
import sys

X = int(input().strip())
#-----

for a in range(-118,120):
    for b in range(-118,120):
        if (a**5 - b**5) == X:
            print(a,b)
            sys.exit()
