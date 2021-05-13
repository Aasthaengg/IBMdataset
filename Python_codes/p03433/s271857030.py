#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 05:50:12 2020

@author: baddude
"""


ttl = int(input())
no_1yen = int(input())

remain = ttl % 500
if no_1yen >= remain:
    print('Yes')
else:
    print('No')
