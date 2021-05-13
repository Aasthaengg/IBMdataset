#!/usr/bin/env python3

S = list(input())
count = {}
count['a'] = S.count('a')
count['b'] = S.count('b')
count['c'] = S.count('c')

if abs(count['a']-count['b']) < 2 and abs(count['a']-count['c']) < 2 and abs(count['b']-count['c']) < 2:
    print('YES')
else:
    print('NO')
