#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    count = int(input())
    colorStr = input()
    res = 0
    for p in colorStr:
        if(p == 'R'):
            res = res + 1
        elif(p == 'B'):
            res =res -1
        else:
            break

    if (res > 0):
        print('Yes')
    else:
        print('No')