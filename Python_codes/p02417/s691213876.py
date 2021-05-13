# -*- coding: utf-8 -*-

import sys
import os
from collections import defaultdict



alphabets = 'abcdefghijklmnopqrstuvwxyz'
d = defaultdict(int)

for s in sys.stdin:
    for c in s:
        c2 = c.lower()
        if c2 in alphabets:
            d[c2] += 1

for c in alphabets:
    print('{} : {}'.format(c, d[c]))