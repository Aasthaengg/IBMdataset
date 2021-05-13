#!/usr/local/bin python
# -*- coding: utf-8 -*-
#
# ~/PycharmProjects/atcoder/A-Parking.py
#
n, a, b = map(int, input().split())
planA = n * a
planB = b
if planA >= planB:
    print(planB)
else:
    print(planA)