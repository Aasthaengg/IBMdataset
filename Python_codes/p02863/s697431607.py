ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

n,t =ma()
AB = []
am = 0
for i in range(n):
    a,b = ma()
    AB.append((a,b))
    am = max(am,a)

dp1 = [[0]*t for i in range(n+1)] #dp1[i][j] 0~i種類までで時間jまでに食べきれる最高スコア
for i in range(n):
    a,b = AB[i]
    #print(a,b)
    for j in range(t-1,-1,-1):
        dp1[i][j] = dp1[i-1][j]
        if j+a<t:
            dp1[i][j+a] = max(dp1[i-1][j]+b,dp1[i][j+a])

dp2 = [[0]*t for i in range(n+1)] ##dp2[i][j] i~n-1種類までで時間jまでに食べきれる最高スコア

for i in range(n):
    a,b = AB[n-i-1]
    for j in range(t-1,-1,-1):
        dp2[n-i-1][j] = dp2[n-i][j]
        if j+a<t:
            dp2[n-i-1][j+a] = max(dp2[n-i][j]+b,dp2[n-i-1][j+a])

tmp=0
for i in range(n):
    for j in range(t):
        tmp = max(tmp,AB[i][1] + dp1[i-1][j] +dp2[i+1][t-1-j])
print(tmp)
