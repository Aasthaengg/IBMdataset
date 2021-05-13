# -*- coding: utf-8 -*-
import sys

N = int(input())
A = [int(input()) for _ in range(N)]


flag = False
for a in A:
    if a%2 == 1:
        flag = True
        break

if flag:
    print('first')
else:
    print('second')