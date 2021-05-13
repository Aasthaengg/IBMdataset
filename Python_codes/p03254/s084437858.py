# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for y in a:
    if y<=x:
        ans+=1
        x-=y
if ans==N and x>0:
    ans-=1
print(ans)