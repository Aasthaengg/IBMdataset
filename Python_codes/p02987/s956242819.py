#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc126/tasks/abc132_a

word = input()
dic_char = {}
for s in word:
    if s in list(dic_char.keys()):
        dic_char[s] += 1
    else:
        dic_char[s] = 1

check = True
for s, count in dic_char.items():
    if count != 2:
        check = False

if check:
    print('Yes')
else:
    print('No')