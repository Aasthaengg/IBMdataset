# -*- coding: utf-8 -*-

S = list(str(input()))

S_num = len(set(S))

if S_num == len(S):
    print('yes')
else:
    print('no')