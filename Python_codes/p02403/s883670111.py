# -*- coding: utf-8 -*-

import sys

rectangle = []
h,w = 1,1

while not(h == 0 and w == 0):
    h,w = map(int, input().split())
    rectangle.append([h,w])

l = len(rectangle)
count = 0

for rec in rectangle:
    count += 1
    for row in range(rec[0]):
        for col in range(rec[1]):
            sys.stdout.write('#')
        print('')
    if (count < l):
        print('')