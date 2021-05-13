# -*- coding:utf-8 -*-
arr = [[[0 for i3 in range(10)] for i2 in range(3)] for i1 in range(4)]

n = int(input())
for i in range(n):
    b,f,r,v = map(int,input().split())
    arr[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(' ',arr[i][j][k],sep = '',end='')
        print('')
    if i != 3:
        print('####################')