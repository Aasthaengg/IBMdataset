#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
l=map(int,raw_input().split())
n=int(raw_input())
ans=chk=0


def rolling(word,dice):
    if word=='S':
        dice[0],dice[1],dice[5],dice[4]=dice[4],dice[0],dice[1],dice[5]
    elif word=='N':
        dice[0],dice[1],dice[5],dice[4]=dice[1],dice[5],dice[4],dice[0]
    elif word=='W':
        dice[0],dice[2],dice[5],dice[3]=dice[2],dice[5],dice[3],dice[0]
    else:
        dice[0],dice[2],dice[5],dice[3]=dice[3],dice[0],dice[2],dice[5]
    return dice

def face(x,y,dice):
    if (x==dice[5] and y==dice[4])or(x==dice[4] and y==dice[0])or(x==dice[0] and y==dice[1])or(x==dice[1] and y==dice[5]):
        return dice[2]
    elif (x==dice[0] and y==dice[2])or(x==dice[2] and y==dice[5])or(x==dice[5] and y==dice[3])or(x==dice[3] and y==dice[0]):
        return dice[4]
    elif (y==dice[5] and x==dice[4])or(y==dice[4] and x==dice[0])or(y==dice[0] and x==dice[1])or(y==dice[1] and x==dice[5]):
        return dice[3]
    elif (y==dice[0] and x==dice[2])or(y==dice[2] and x==dice[5])or(y==dice[5] and x==dice[3])or(y==dice[3] and x==dice[0]):
        return dice[1]
    elif (x==dice[2] and y==dice[1])or(x==dice[1] and y==dice[3])or(x==dice[3] and y==dice[4])or(x==dice[4] and y==dice[2]):
        return dice[5]
    else:
        return dice[0]
        

for i in range(n):
    a,b=map(int,raw_input().split())
    print face(a,b,l)