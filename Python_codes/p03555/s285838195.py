# -*- coding: utf-8 -*-

c1 = list(str(input()))
c2 = list(str(input()))

l = [c1, c2]
ll = [[x for x in reversed(c2)] , [x for x in reversed(c1)]]

if l == ll:
    print('YES')
else:
    print('NO')