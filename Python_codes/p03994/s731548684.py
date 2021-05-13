# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

a=ord('a')
S=list(map(lambda x:ord(x)-a,input()))
K=int(input())
ans=[]
for x in S:
    if x==0:
        ans.append('a')
    elif 26-x<=K:
        ans.append('a')
        K-=26-x
    else:
        ans.append(chr(x+a))
if K>0:
    ans[-1]=chr((ord(ans[-1])-a+K)%26+a)
print(''.join(ans))