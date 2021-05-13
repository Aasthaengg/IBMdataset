# -*- coding: utf-8 -*-

[A, B, C, D] = [int(i) for i in input().split()]

left = A + B
right = C + D

if left > right:
    print('Left')
elif left == right:
    print('Balanced')
else:
    print('Right')
