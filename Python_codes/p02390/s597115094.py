#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def time(s):
    h = s / 3600
    m = (s - (h * 3600)) / 60
    s = (s - (h * 3600)) - (m * 60)
    h, m, s = map(str, (h, m, s))
    print "%s:%s:%s" % (h, m, s)

s = int(raw_input())

if 0 <= s <= 86400:
    time(s)
else:
    sys.exit(0)