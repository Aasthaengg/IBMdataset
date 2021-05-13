# -*- coding: utf-8 -*-
import sys
N,K=map(int, sys.stdin.readline().split())
S=sys.stdin.readline().strip()
L=[]
cnt=0
for i,x in enumerate(S):
    if i==0:
        cnt+=1
        prev=x
    else:
        if prev==x: #前の文字と今の文字が同じ
            cnt+=1
        else:       #前の文字と今の文字が異なる
            L.append(cnt)
            cnt=1
        prev=x
else:
    L.append(cnt)

print sum(L)-max(1,len(L)-2*K)
