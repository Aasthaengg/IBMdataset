from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

Given_num=int(input())
tmp_num=int(input())
minv=tmp_num
maxv=-BIG_NUM
for i in range(1,Given_num):
    tmp_num=int(input())
    maxv=max(maxv,tmp_num-minv)
    minv=min(minv,tmp_num)
print("%d"%(maxv))

