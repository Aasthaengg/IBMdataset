#!/usr/bin/env python3
s = input()
a=0<int(s[:2])<13
b=0<int(s[-2:])<13
if a and b:
    print('AMBIGUOUS')
elif b:
    print('YYMM')
elif a:
    print('MMYY')
else:
    print('NA')
