# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N,M=map(int,input().split())
x=tuple(map(int,input().split()))
y=tuple(map(int,input().split()))
ans=1
tmp=0
for i in range(N):
    tmp+=x[i]*(i-(N-1-i))
    tmp%=MOD
ans*=tmp
tmp=0
for i in range(M):
    tmp+=y[i]*(i-(M-1-i))
    tmp%=MOD
ans*=tmp
ans%=MOD
print(ans)