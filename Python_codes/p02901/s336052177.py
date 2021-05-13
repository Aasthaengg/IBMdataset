# -*- coding: utf-8 -*-
n,m = list(map(int,input().split()))
price = [0] * m
can_opens = [0] * m
for i in range(m):
    a,b = list(map(int,input().split()))
    price[i]=a
    c = ["0"] * n
    ci = list(map(int,input().split()))
    for j in ci:
        c[n- j]="1"
    can_opens[i]=int("".join(c),2)
inf=float("inf")
dp = [inf] * 2**n
dp[0]=0
#dp[i]は、iを取るために必要な最小費用
for i,(pi,coi) in enumerate(zip(price,can_opens)):
    for j in range(2**n):
        dp[j|coi]=min(dp[j|coi],dp[j]+pi)
from math import isinf
if isinf(dp[-1]):
    print(-1)
else:
    print(dp[-1])