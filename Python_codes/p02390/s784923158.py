#!/usr/bin/python
# -*- coding: utf-8 -*-


s = input()
h = s/3600
m = s%3600/60
s = s%3600%60

print "%d:%d:%d" % (h,m,s)