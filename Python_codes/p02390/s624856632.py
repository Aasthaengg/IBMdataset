#!/usr/bin/env python
# -*- coding: utf-8 -*-

S = int(input())
h = S//3600
m = (S - h*3600)//60
s = (S - h*3600 - m*60)
print('%d:%d:%d' % (h, m ,s))