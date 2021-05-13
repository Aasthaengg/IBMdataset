# -*- coding: utf-8 -*-
n = int(input())
a = [int(i) for i in input().split()] 

tmp = 1
for i in a:
    if i % 2 == 1:
        tmp *= 1
    else:
        tmp *= 2
print(pow(3, n) - tmp)
