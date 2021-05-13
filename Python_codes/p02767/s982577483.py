"""Boot-camp-for-Beginners_002_C_Rally_19-August-2020.py"""
import numpy as np
import sys

N=int(input())
X = list(map(int,input().split()))
s=0
for i in range(len(X)):
    s+=X[i]
P=int(s/N)

Sum_round_down=0
Sum_round_up=0
for i in range(len(X)):
    Sum_round_down+=(P-X[i])**2
    Sum_round_up+=(P+1-X[i])**2
if(Sum_round_down>=Sum_round_up):
    Sum=Sum_round_up
else:
    Sum=Sum=Sum_round_down
print(int(Sum))