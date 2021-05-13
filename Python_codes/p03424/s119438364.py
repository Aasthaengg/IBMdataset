# -*- coding: utf-8 -*-

N = int(input())
S = list(map(str, input().split()))

set_S = set(S)

if len(set_S) == 3:
    print('Three')
else:
    print('Four')