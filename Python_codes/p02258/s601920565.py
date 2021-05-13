#!/usr/bin/env python
#-*- coding:utf-8 -*-

N = int(raw_input())

R = [int(raw_input()) for _ in range(N)]

minR = R[0]
maxVal = -2000000000

for i in R[1::]:
    maxVal = max(maxVal,i - minR)
    minR = min(minR, i)

print maxVal