#!/usr/bin/env python
# -*- coding: utf-8 -*-

S = input().strip()
result = 0
num = list()
for i in range(len(S)):
    num.append(int(S[i]))

for b in range(2**(len(S)-1)):
    b_str = format(b, 'b').zfill(len(S)-1)
    sum = 0
    for i in range(len(num) - 1):
        if b_str[i] == '0':
            result += sum * 10 + num[i]
            sum = 0
        else:
            sum = sum * 10 + num[i]
    result += sum * 10 + num[-1]

print(result)

