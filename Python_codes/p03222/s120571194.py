#import decimal
#decimal.getcontext().prec==500 Floatの桁数を500まで増やす
#Decimal(c).sqrt() それで平方根を求める
#Decimal(1) / Decimal(7) 1/7

from collections import *
from itertools import *
from bisect import *
from heapq import *
import copy
import math
from fractions import gcd
import sys
#input = sys.stdin.readline

H,W,K=map(int,input().split())
mod=10**9+7
if W==1:
    print(1)
    exit()
dp=[[0 for i in range(W)] for h in range(H+1)]
dp[0][0]=1

for h in range(1,H+1):
    for i in range(2**(W-1)):
        #print(h,i)
        lst=[i>>m&1 for m in range(W-1)]
        for w in range(len(lst)-1):
            if lst[w]==lst[w+1]==1:
                break
        else:
            #print(h,lst)
            for w in range(W):
                if w>0 and lst[w-1]:
                    dp[h][w]+=dp[h-1][w-1]
                elif w<len(lst) and lst[w]:
                    dp[h][w]+=dp[h-1][w+1]
                else:
                    dp[h][w]+=dp[h-1][w]
        for _ in range(len(dp[0])):
            dp[h][_]%=mod
#print(sum(dp[-1]))
print(dp[-1][K-1]%mod)
