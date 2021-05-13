# -*- coding: utf-8 -*-
H, W=map(int,input().split())
s=[[0]*(W+2) for i in range(H+2)]
for ii in range(1,H+1):
    A=list(input())
    for jj in range(1,W+1):
        if A[jj-1]=='#':
            s[ii][jj]=1
can=1
for ii in range(1,H+1):
    for jj in range(1,W+1):
        if s[ii][jj]==1:
            if s[ii-1][jj]+s[ii+1][jj]+s[ii][jj-1]+s[ii][jj+1]==0:
                can=0
                break
    if can==0:
        break

if can==1:
    print('Yes')
else:
    print('No')
            
