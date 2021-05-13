# -*- coding: utf-8 -*-

import sys
import os


N = int(sys.stdin.readline())
lines = sys.stdin.readlines()
d = {}
for s in lines:
    command, word = s.split()
    if command == 'insert':
        d[word] = True
    elif command == 'find':
        if word in d.keys():
            print('yes')
        else:
            print('no')