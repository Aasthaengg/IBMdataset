#!/usr/bin/python
# -*- coding: utf-8 -*-

A,B,M = map(int,input().split())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
xyc = []
for _ in range(0,M):
    xyc.append([int(x) for x in input().split()])

ans = 0

ans = min(a) + min(b)

coupon = []

for i in range(0,M):
    coupon.append(a[xyc[i][0]-1] + b[xyc[i][1]-1] - xyc[i][2])

ans = min(ans,min(coupon))

print(ans)