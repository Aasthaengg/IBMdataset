# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 17:18:51 2015

@author: hirose
"""

#Repetitive Processing - Print Test Cases
i = 1
while 1:
    n = int(raw_input())
    if(n != 0):
        print 'Case %(1)d: %(2)d'  % {'1':i, '2':n}
        i += 1
    else:
        break