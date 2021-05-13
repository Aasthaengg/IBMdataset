#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

s = sys.stdin.readline()
for c in s:
    if c.islower():
        print(c.upper(), end='')
    elif c.isupper():
        print(c.lower(), end='')
    else:
        print(c, end='')

