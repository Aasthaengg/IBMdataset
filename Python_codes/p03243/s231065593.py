# -*- coding: utf-8 -*-
N = int(input())
for i in range(10):
    num = 100*i+10*i+i
    if num>=N:
        print(num)
        break
