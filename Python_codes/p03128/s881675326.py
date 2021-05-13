#2 5 5 4 5 6 3 7 6
#ナップザックのdpかな
#dp[i][v] = dp[i-A[i]][v-M[i]*(10*i)]

import sys
import math 
ni = lambda: int(ns())
na = lambda: list(map(int, input().split()))
ns = lambda: input()

N,M = na()
A = na()
cost = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

d = {i:cost[i] for i in A}

dp = [-1]*(N+1)
dp[0] = 0
ans = [0]*(N+1)
for i in range(N+1):
    for j in range(10)[::-1]:
        if j not in d:
            continue
        elif d[j] > i:
            continue
        else:
            #print(j)
            if dp[i] < dp[i-d[j]]+1:
                dp[i] = dp[i-d[j]]+1
                ans[i] = j
S = ""
pos = N
#print(dp,ans)
while pos!=0:
    #print(pos)
    S+=str(ans[pos])
    pos-=d[ans[pos]]


print(S)