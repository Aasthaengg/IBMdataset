# -*- coding: utf-8 -*-

c1 = list(str(input()))
c2 = list(str(input()))

l = [c1, c2]
ll = [[c2[2], c2[1], c2[0]] , [c1[2], c1[1], c1[0]]]

if l == ll:
    print('YES')
else:
    print('NO')