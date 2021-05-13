# -*- coding: utf-8 -*-
import math

#入力
a, b, c = map(int, input().split())

list = []
list.append(a)
list.append(b)
list.append(c)

list.sort()

print (list[0] + list[1])