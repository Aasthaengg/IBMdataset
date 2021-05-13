#-*- coding:utf-8 -*-
import numpy as np

s = input()
list_s = list(s)

count=0
for i in list_s:
    if i == '2':
        count+=1

print(count)