# -*- coding: utf-8 -*-

l = sorted(list(map(int, input().split())))

if sum(l[0:2]) == l[-1]:
    print('Yes')
else:
    print('No')