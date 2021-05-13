#
import sys
import math
import numpy as np
import itertools

# いくつか入力
n,m = (int(i) for i in input().split())

if m % 2 == 0:
    for i in range(0,m//2):
        print(i+1,m+1-i)
    for i in range(m//2,m):
        print(m//2+2+i,m*2+m//2+1-i)
else:
    for i in range(0,m//2):
        print(i+1,m-i)
    for i in range(m//2+1,m+1):
        print(m//2+1+i,m*2+m//2+2-i)
