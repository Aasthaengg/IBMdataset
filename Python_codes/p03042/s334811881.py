#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = int(input())
a = s // 100
b = s % 100
if 1 <= a <= 12:
    if 1 <= b <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if 1 <= b <= 12:
        print('YYMM')
    else:
        print('NA')