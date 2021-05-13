#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

w = sys.stdin.readline().strip().lower()

num_w = 0

while True:
    s_lst = sys.stdin.readline().split()
    if s_lst[0] == 'END_OF_TEXT':
        break
    for str_x in s_lst:
        str_x = str_x.lower()
        if str_x == w:
            num_w += 1

print(num_w)

