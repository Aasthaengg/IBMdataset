#! /usr/bin/env python
# -*- coding: utf-8 -*-

l = []
while True:
    values = map(int, raw_input().split())
    if values[0] == 0 and values[1] == 0:
        break
    else:
        l.append(values)

for v in l:
    if v[0] < v[1]:
        print('%d %d') % (v[0], v[1])
    else:
        print('%d %d') % (v[1], v[0])