# -*- coding: utf-8 -*-

import sys

rectangle = []
h,w = 1,1

while not(h == 0 and w == 0):
    h,w = map(int, input().split())
    if not(h == 0 and w == 0):
        rectangle.append([h-2,w-2])

for rec in rectangle:

    display = []

    for col in range(rec[1] + 2):
        display.append('#')
    
    display.append('\n')
    
    for row in range(rec[0]):
        
        display.append('#')
        for col in range(rec[1]):
            display.append('.')
        display.append('#')
        display.append('\n')
    
    for col in range(rec[1] + 2):
        display.append('#')
    display.append('\n')
    print(''.join(display))