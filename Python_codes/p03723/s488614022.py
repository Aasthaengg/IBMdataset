# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

l=list(map(int,input().split()))
for i in range(10**6):
    for k in range(3):
        if l[k]%2:
            print(i)
            exit()
    a=[0]*3
    for k in range(3):
        a[k]=(l[(k+1)%3]+l[(k+2)%3])//2
    l=a
print(-1)