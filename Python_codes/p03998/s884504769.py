import bisect,copy,heapq,string
from collections import *
from math import *
from itertools import *
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

a = input()
b = input()
c = input()
i = j = k = -1
sel = 'a'

while i<len(a) and j<len(b) and k<len(c):
        if sel == 'a':
                i += 1
                if i < len(a):
                        sel = a[i]
        elif sel == 'b':
                j += 1
                if j < len(b):
                        sel = b[j]
        elif sel == 'c':
                k += 1
                if k < len(c):
                        sel = c[k]

if i == len(a):
        print('A')
elif j == len(b):
        print('B')
elif k == len(c):
        print('C')