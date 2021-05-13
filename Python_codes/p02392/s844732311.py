# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:07:27 2018

@author: Fujiichang
"""

if __name__ == "__main__":

    x = map(int, raw_input().split())
    a = x[0]
    b = x[1]
    c = x[2]

    if a < b:
        if b < c:
            print 'Yes'
        else:
            print 'No'

    else:
        print 'No'

