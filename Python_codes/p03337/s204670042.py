# -*- coding: utf-8 -*-
import math

#入力
#S = str(input())
A, B = map(int, input().split())
#N = int(input())

list = []
list.append(A + B)
list.append(A - B)
list.append(A * B)
list.sort()

print (list[2])