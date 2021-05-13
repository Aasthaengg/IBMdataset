# -*- coding: utf-8 -*-
import sys
from math import gcd
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
A=list(map(int,input().split()))
ans=A[0]
for x in A[1:]:
    ans=gcd(ans,x)
print(ans)