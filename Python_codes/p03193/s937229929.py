# -*- coding: utf-8 -*-

from sys import stdin

n,h,w = [int(x) for x in stdin.readline().split()]
data = [[int(x) for x in stdin.readline().split()] for i in range(n)]

count = 0
for h0, w0 in data:
    if h0 >= h and w0 >= w:
        count += 1

print(count)
