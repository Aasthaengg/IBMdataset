# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math

N,M=map(int,input().split())
xyz=[list(map(int,input().split())) for m in range(N)]
dp=[[[0,0] for i in range(M)] for i in range(N)]
if M==0:
    print(0)
    exit()
num=0
for a in [-1,1]:
    for b in [-1,1]:
        for c in [-1,1]:
            dp=[[None for m in range(M)] for i in range(N)]
            for i in range(0,N):
                x,y,z=xyz[i]
                A=x*a+y*b+z*c
                #print(dp)
                if i==0:
                    dp[i][0]=A
                else:
                    for m in range(0,M):
                        if m==0:
                            dp[i][m]=max(dp[i-1][m],A)
                        else:
                            if dp[i-1][m]:
                                dp[i][m]=max(dp[i-1][m-1]+A,dp[i-1][m])
                            elif dp[i-1][m-1]:
                                dp[i][m]=dp[i-1][m-1]+A
                            else:
                                break
            if dp[-1][-1]:
                num=max(dp[-1][-1],num)
print(num)
