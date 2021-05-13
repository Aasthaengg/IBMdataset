# -*- coding: utf-8 -*-

s = sorted(list(str(input())))
t = sorted(list(str(input())), reverse=True)

if ''.join(s) < ''.join(t):
    print('Yes')
else:
    print('No')