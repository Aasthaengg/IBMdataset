# -*- coding: utf-8 -*-

import sys
import os


s = input().strip()
q = input().strip()

s = s + s
if q in s:
    print('Yes')
else:
    print('No')