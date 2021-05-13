# -*- coding: utf-8 -*-

list = map(int, raw_input().split())
a = list[0]
b = list[1]
c = list[2]

if a < b and b < c:
    print "Yes"
else:
    print "No"