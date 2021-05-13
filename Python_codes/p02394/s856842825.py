# -*- coding:utf-8 -*-

array = input()
array = array.split()
for i in range(len(array)):
    array[i] = float(array[i])

W,H,x,y,r = array[0],array[1],array[2],array[3],array[4]

if x-r >= 0 and y+r <= H and x+r <= W and y-r >= 0:
    print('Yes')
else:
    print('No')