# -*- coding: utf-8 -*-

list = map(str, raw_input().split())
num = []
for i in list:
    if i == '+':
        num[len(num)-2] += num.pop()
    elif i == '-':
        num[len(num)-2] -= num.pop()
    elif i == '*':
        num[len(num)-2] *= num.pop()
    else:
        num.append(int(i))
print num[0]