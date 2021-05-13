# -*- coding: utf-8 -*-

n = list(str(input()))

if n[0:3].count(n[0]) == 3 or n[1:].count(n[1]) == 3:
    print('Yes')
else:
    print('No')