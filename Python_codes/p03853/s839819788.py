# -*- coding: utf-8 -*-

h, w = map(int, input().split())
rct = []

for x in range(h):
    pix = str(input())
    rct.append(pix)
    rct.append(pix)

print(*rct, sep='\n')