# -*- coding:utf-8 -*-

num = int(input())
min = 0
sa = -10000000000
for i in range(num):
    atai = int(input())
    if i == 0:
        min = atai
        continue
    sa_temp = atai - min
    if sa < sa_temp:
        sa = sa_temp
    if min > atai:
        min = atai
print(sa)