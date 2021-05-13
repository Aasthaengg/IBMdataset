# -*- coding: utf-8 -*-

import sys

i = 0
for line in sys.stdin:
    if line[0] == "0":
        break
    i += 1
    print "Case %s: %s" %(i, line),