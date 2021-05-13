#!/usr/bin/env python3

s = input()
d = {'a': 0, 'b': 0, 'c': 0}
for i in s:
    d[i] += 1

# print(d)

if ((d['a']==d['b'] and d['b']==d['c']) or \
    (d['a']==d['b']+1 and d['b']==d['c']) or \
    (d['b']==d['a']+1 and d['a']==d['c']) or \
    (d['c']==d['a']+1 and d['a']==d['b']) or \
    (d['a']==d['b'] and d['a']==d['c']+1) or \
    (d['a']==d['c'] and d['a']==d['b']+1) or \
    (d['b']==d['c'] and d['b']==d['a']+1)):
    print('YES')
else:
    print('NO')
