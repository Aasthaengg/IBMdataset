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
dp=[[idle_max for m in range(403*400)] for i in range(N)]
used=set()
a,b,c=ABC[0]
dp[0][a*401+b]=c
for n in range(1,N):
    a,b,c=ABC[n]
    for i in range(len(dp[0])):
        if i-(a*401+b)>=0 and dp[n-1][i-(a*401+b)]!=idle_max:
            dp[n][i]=min(dp[n-1][i-(a*401+b)]+c,dp[n-1][i])
        else:
            dp[n][i]=dp[n-1][i]
    dp[n][a*401+b]=min(dp[n-1][a*401+b],c)

value=idle_max
for i in range(len(dp[0])):
    if dp[-1][i]:
        A=i//401;B=i%401
        if A and B:
            Z=gcd(A,B)
            A//=Z;B//=Z
            if Ma==A and Mb==B:
                value=min(value,dp[-1][i])
if value!=idle_max:
    print(value)
else:
    print(-1)
