#!/usr/bin/env python3

import sys
input=sys.stdin.readline

r,c,k=map(int,input().split())
items=[0]*(r*c)
for _ in range(k):
    tr,tc,tv=map(int,input().split())
    items[c*(tr-1)+tc-1]=tv
dp=[0]*(4*r*c)
for i in range(1,r+1):
    for j in range(1,c+1):
        tv=items[c*(i-1)+j-1]
        change_pos=4*(c*(i-1)+j-1)
        left_pos=4*(c*(i-2)+j-1)
        up_pos=4*(c*(i-1)+j-2)
        if i!=1:
          left_max=max(dp[left_pos],dp[left_pos+1],dp[left_pos+2],dp[left_pos+3])
        else:
          left_max=0
        if j!=1:
          dp[change_pos]=max(dp[up_pos],left_max)
          dp[change_pos+1]=max(dp[up_pos+1],dp[up_pos]+tv,left_max+tv)        
          dp[change_pos+2]=max(dp[up_pos+2],dp[up_pos+1]+tv)
          dp[change_pos+3]=max(dp[up_pos+3],dp[up_pos+2]+tv)
        else:
          dp[change_pos]=left_max
          dp[change_pos+1]=left_max+tv
print(max(dp[-1],dp[-2],dp[-3],dp[-4]))