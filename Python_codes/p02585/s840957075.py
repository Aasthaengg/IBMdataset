import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
MOD = 10**9+7

N,K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))

sumlist1 = [[0]*N for _ in range(N)]
walist = [[0]*N for _ in range(N)]
loopcount = [0]*N

for h in range(N):
    sumlist1[h][0] = C[h]
    walist[h][0] = C[h]
    now = h
    l = 0
    for i in range(1,N):
        now = P[now]-1

        if sumlist1[h][i-1] < 0:
            sumlist1[h][i] = C[now]
        else:
            sumlist1[h][i] += sumlist1[h][i-1] + C[now]
        walist[h][i] += walist[h][i-1] + C[now]
        
        l += 1
        if now == h:
            break
    else:
        l += 1
    loopcount[h] = l
#print(sumlist1)

maxlist = [0]*N
for i in range(N):
    T = loopcount[i]
    wa = walist[i][T-1]
    #print(wa,T)

    loop = K//T
    amari = K%T

    if wa >= 0:
        if loop == 0:
            if amari != 0:
                maxlist[i] = wa*loop + max(sumlist1[i][:amari])
            else:
                maxlist[i] = max(sumlist1[i][:amari])
        else:
            if amari != 0:
                maxlist[i] = max(wa*loop + max(sumlist1[i][:amari]), wa*(loop-1) + max(sumlist1[i]))
            else:
                maxlist[i] = max(wa*loop, wa*(loop-1) + max(sumlist1[i][:T]))
            

    else:
        if loop == 0:
            maxlist[i] = max(sumlist1[i][:amari])
        else:
            maxlist[i] = max(sumlist1[i])

print(max(maxlist))
#print(sumlist1)