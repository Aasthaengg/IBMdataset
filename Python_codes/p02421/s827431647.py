#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?????????????????£?????????
"""
turns = int(input().strip())
hanako = 0
tarou = 0
for i in range(turns) :
   tcard, hcard = input().strip().split()

   if tcard == hcard :
       hanako += 1
       tarou += 1
   elif tcard > hcard :
       tarou += 3
   else:
       hanako += 3

print("{0} {1}".format(tarou,hanako))