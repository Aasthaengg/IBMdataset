#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

s = s + s

if p in s:
    print('Yes')
else:
    print('No')

