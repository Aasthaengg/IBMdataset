#!/usr/bin/env python
# -*- coding: utf-8 -*-

a, b = map(int, input().split())
d = a//b
r = a%b
f = a/b
print('%d %d %.8f' % (d, r, f))