#!/usr/bin/env python
# -*- coding: utf-8 -*-

S = input().strip()
res = 7
num = list()
for i in range(len(S)):
    num.append(int(S[i]))

for b in range(2**(3)):
    b_str = format(b, 'b').zfill(len(S)-1)
    sum = num[0]
    for i in range(len(num) - 1):
        if b_str[i] == '0':
            sum -= num[i+1]
        else:
            sum += num[i+1]
    if sum == res:
        break

plus_or_minus = list()
for i in range(3):
    if b_str[i] == '0':
        plus_or_minus.append('-')
    else:
        plus_or_minus.append('+')
print('{}{}{}{}{}{}{}=7'.format(num[0], plus_or_minus[0], num[1], plus_or_minus[1], num[2], plus_or_minus[2], num[3]))
