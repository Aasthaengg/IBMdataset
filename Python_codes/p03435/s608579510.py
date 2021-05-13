# -*- coding: utf-8 -*-
C=[[0]*3 for i in range(3)]
for ii in range(3):
    C[ii]=list(map(int,input().split()))

#Flag=0

#if C[0][0]-C[1][0]==C[0][1]-C[1][1] and C[0][1]-C[1][1]==C[0][2]-C[1][2] and C[1][0]-C[2][0]==C[1][1]-C[2][1] and C[1][1]-C[2][1]==C[1][2]-C[2][2]:
#    Flag=1
Flag=1
for ii in range(1,3):
    for jj in range(1,3):
        if C[ii-1][jj-1]-C[ii][jj-1]!=C[ii-1][jj]-C[ii][jj]:
            Flag=0
            break
    if Flag==0:
        break

if Flag==1:
    print('Yes')
else:
    print('No')
