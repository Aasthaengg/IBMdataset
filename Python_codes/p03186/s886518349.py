#! /usr/bin/env python3
# -*- coding: utf-8 -*-

A, B, C = [int(x) for x in input().split()]

if B >= C-1:
    answer = C + B
elif (B+A) >= C-1:
    answer = B + C
else:
    answer = 2*B + A+1

print(answer)