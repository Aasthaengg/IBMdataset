#!/usr/local/bin python
# -*- coding: utf-8 -*-
#
# ~/PycharmProjects/atcoder/B-problems/ChristmasEveEve.py
#
n = int(input())
p = list()
for i in range(n):
    pi = int(input())
    p.append(pi)

print(int(sum(p)-max(p)/2))