# -*- coding: utf-8 -*-
loop = 1
while(loop):
    l = input().strip().split()
    H = int(l[0])
    W = int(l[1])
    if(H == 0 and W == 0):
        break
    else:
        for y in (range(H)):
            str = "#" * W
            print(str)
        print()