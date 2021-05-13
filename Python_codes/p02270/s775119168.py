from collections import deque
from enum import Enum
import sys
import math
 
BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001
 
 
N,K = map(int,input().split())
 
table = [0]*N
max_W = 0
 
for i in range(N):
    table[i] = int(input())
    max_W = max(max_W,table[i])
 
 
left = max_W;right = 10000*100000;mid = (left+right)//2;
ans = right
 
 
def is_ok(tmp_P):
 
    num_track = 1
    tmp_sum = 0
    for i in range(N):
 
        if tmp_sum+table[i] <= tmp_P:
            tmp_sum += table[i]
        else:
            num_track += 1
            tmp_sum = table[i]
            if num_track > K:
                return False
 
    return True
 
 
while left <= right:
 
    if is_ok(mid) == True:
        ans = mid
        right = mid-1
    else:
        left = mid+1
 
    mid = (left+right)//2;
 
 
print("%d"%(ans))
