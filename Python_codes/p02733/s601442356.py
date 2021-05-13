# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

H,W,K=map(int,input().split())
S=[list(map(int,list(input()))) for _ in range(H)]
ans=INF
for i in range(2**(H-1)):
    cnt=1+bin(i).count('1')
    tmp=cnt-1
    div=[0]*H
    for j in range(H-1):
        if (i>>j)&1:
            div[j+1]=div[j]+1
        else:
            div[j+1]=div[j]
    wc=[0]*cnt
    for x in range(W):
        tmp_wc=[0]*cnt
        f=False
        for y in range(H):
            if S[y][x]==1:
                tmp_wc[div[y]]+=1
                wc[div[y]]+=1
                if wc[div[y]]>K:
                    f=True
                if tmp_wc[div[y]]>K:
                    break
        else:
            if f:
                tmp+=1
                wc=tmp_wc
                tmp_wc=[0]*cnt
                f=False
            continue
        break
    else:
        ans=min(ans,tmp)
print(ans)