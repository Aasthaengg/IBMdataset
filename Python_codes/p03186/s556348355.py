# -*- coding: utf-8 -*-
A, B, C = map(int, input().split(' '))
if A + B >= C:
    print(B + C)
else:
    C -= A + B
    ret = A + B + B
    if C > 0:
        ret += 1

    print(ret)



