# -*- coding: utf-8 -*-
S = input()

if 2 == len(S):
    print(S)
elif 3 == len(S):
    print(S[::-1])
else:
    print("other")