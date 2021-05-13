#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import io
import re
import math

while True:
#    i = 0
    n = int(raw_input())
    if n==0: break
    l = map(float, raw_input().split())
# hyojunhensa**2 = sum(tokuten-heikinten)**2)/ninzu
    avg=sum(l)/len(l)
    naka=0
    for i in l:
        naka+=(i-avg)**2
    hyo2 = naka/n
    print (hyo2)**0.5