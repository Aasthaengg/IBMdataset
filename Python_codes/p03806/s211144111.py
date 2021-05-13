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


#N=int(input())

N,Ma,Mb=map(int,input().split())
ABC=[list(map(int,input().split())) for i in range(N)]
idle_max=10**9
dp=[[[idle_max for b in range(400)] for a in range(400)] for i in range(N)]
used=set()
a,b,c=ABC[0]
dp[0][a][b]=c

for n in range(1,N):
    a,b,c=ABC[n]

    for x in range(400):
        for y in range(400):
            if x-a>=0 and y-b>=0 and dp[n-1][x-a][y-b]!=idle_max:
                dp[n][x][y]=min(dp[n-1][x-a][y-b]+c,dp[n-1][x][y])
            else:
                dp[n][x][y]=dp[n-1][x][y]
    dp[n][a][b]=min(dp[n-1][a][b],c)
value=idle_max
for x in range(1,400):
    for y in range(1,400):
        z=gcd(x,y)
        a=x//z;b=y//z
        if Ma==a and Mb==b:
            value=min(dp[-1][x][y],value)

if value!=idle_max:
    print(value)
else:
    print(-1)
