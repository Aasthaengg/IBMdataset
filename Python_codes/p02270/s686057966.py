from enum import Enum
from queue import Queue
import collections

import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

global n,k
global ws

def iSok(Pmax):
    truck = 0
    now = 0
    for i in range(n):
        if ws[i]>Pmax:
            return False
        if now+ws[i]>Pmax:
            truck += 1
            now = ws[i]
        else:
            now += ws[i]
    if now > 0:
        truck += 1
    if truck > k:
        return False
    else:
        return True

n,k = map(int,input().split())

now = 0
ws = [int(input()) for i in range(n)]
amin = 0
amax = sum(ws)

while amax-amin >1:
    amid = (amin + amax)//2
    if iSok(amid):
        amax = amid
    else:
        amin = amid
print(amax)

