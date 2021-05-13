#from collections import *
#from itertools import *
#from bisect import *
from heapq import *
#import copy
#N=int(input())
#X,Y=map(int,input().split())
#S=list(map(int,input().split()))
#S=[list(map(int,input().split())) for i in range(N)]

N,C=map(int,input().split())
XV=[list(map(int,input().split())) for i in range(N)]
XVR=list(reversed(XV))
value=0
tempvalue=0
csXV=[[0,0] for i in range(N)]
csXVR=[[0,0] for i in range(N)]
csXV[0][0]=XV[0][0]
csXV[0][1]=XV[0][1]
csXVR[0][0]=XV[-1][0]
csXVR[0][1]=XV[-1][1]
csXVR[0][0]=C-csXVR[0][0]
for i in range(1,N):
    csXV[i][0] =XV[i][0]
    csXV[i][1] =XV[i][1]+csXV[i-1][1]
    csXVR[i][0]=C-XV[N-1-i][0]
    csXVR[i][1]=XVR[i][1]+csXVR[i-1][1]


csXV[0].append(csXV[0][1]-csXV[0][0])
csXVR[0].append(csXVR[0][1]-csXVR[0][0])

for i in range(1,N):
    csXV[i].append(csXV[i][1]-csXV[i][0])
    csXVR[i].append(csXVR[i][1]-csXVR[i][0])

csXV[0].append(csXV[0][2])
csXVR[0].append(csXVR[0][2])



for i in range(1,N):
    csXV[i].append(max(csXV[i][2],csXV[i-1][3]))
    csXVR[i].append(max(csXVR[i][2],csXVR[i-1][3]))

#距離、価値、累積価値ー距離、３の累積最大値

value=0
for i in range(N-1):
    B=N-1 -i-1
    tempvalue=csXV[i][2]-csXV[i][0]+csXVR[B][3]
    value=max(tempvalue,value,csXV[i][3])

for i in range(N-1):
    B=N-1 -i-1
    tempvalue=csXVR[i][2]-csXVR[i][0]+csXV[B][3]
    value=max(tempvalue,value,csXV[i][3])

value=max(value,csXV[-1][3],csXVR[-1][3])

print(value)
