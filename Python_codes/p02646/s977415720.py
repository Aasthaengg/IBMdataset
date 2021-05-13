#!/usr/bin/env python3
import sys
import numpy as np
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())
if b==d :
    print('NO')
elif (abs(a-c)/(b-d))<= t and d<b :
    print('YES')
else:
    print('NO')