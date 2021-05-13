#!/usr/bin python3
# -*- coding: utf-8 -*-

n = int(input())
u = [0]*n
v = [0]*n
for i in range(n):
    x, y = map(int, input().split())
    u[i] = x+y
    v[i] = x-y

ret = 0
ret = max(ret, max(u)-min(u))
ret = max(ret, max(v)-min(v))
print(ret)