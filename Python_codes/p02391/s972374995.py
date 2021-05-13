#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = map(int, raw_input().split())
if data[0] < data[1]:
    print "a < b"
elif data[0] == data[1]:
    print "a == b"
else:
    print "a > b"