# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 18:47:21 2015

@author: hirose
"""

#Repetitive Processing - Swapping Two Numbers

while 1:
    n = map(int, raw_input().split())
    x = n[0]
    y = n[1]
    
    if(x==0 and y==0):
        break
    
    if(x <= y):
        print '%(1)d %(2)d' %{'1':x, '2':y}
    else:
        print '%(1)d %(2)d' %{'1':y, '2':x}