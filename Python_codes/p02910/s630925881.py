# -*- coding: utf-8 -*-

s = list(input())

for i, posi in enumerate(s):
    num = i+1
    if num % 2 == 0 and posi == 'R':
        print('No')
        exit(0)
    elif num % 2 != 0 and posi == 'L':
        print('No')
        exit(0)

print('Yes')
