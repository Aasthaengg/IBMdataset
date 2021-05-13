# -*- coding: utf-8 -*-

import sys
import os


s = input().strip()
for c in s:
    if c.islower():
        print(c.upper(), end='')
    elif c.isupper():
        print(c.lower(), end='')
    else:
        print(c, end='')
print()