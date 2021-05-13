#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from __future__ import print_function
import time
import sys
import io
import re
import math
#start = time.clock()
#i = 0
#check = 'insert'
n=input()
a=set()
for x in xrange(n):
    (i,f)=map(str, raw_input().split())
    if i=='insert':
        a.add(f)
    else:
        if f in a:
            print 'yes'
        else:
            print 'no'