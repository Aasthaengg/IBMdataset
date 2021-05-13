# -*- coding: cp932 -*-

import sys
import os
import re
import datetime
import bisect

### main ###

X = input()

restS = []
for c in X:
    #print("c = {}".format(c))
    restS.append(c)
    if c == 'T':
        while(len(restS) >= 2):
            #print("restS = {}, last 2 string = {} ".format(restS, restS[-2:]))
            #if("".join(restS[-2:]) == 'ST'):
            if(restS[-2] == 'S' and restS[-1] == 'T'): # Higher Speed than join ?
                #print("hit restS[-2] = {}, restS[-1] = {}".format(restS[-2], restS[-1]))
                #restS = restS[:-2] # TLE
                del restS[-2:]
                #print("new restS = {}".format(restS))
            else:
                #print("no hit restS = {}".format(restS))
                break # out of while

print(len(restS))