import collections
from collections import deque

h,w= map(int, input().split())
s= [list(input()) for i in range(h)]

# １行目、一列目を囲う
for i in range(h):
    s[i]=['#']+s[i]
s=[['#']*(w+1)]+s

dp=[[0]*(w+1) for i in range(h+1)]
# 各マスに到達する最小の操作回数
for i in range(w+1):
    dp[0][i]+=1
for i in range(h+1):
    dp[i][0]+=1


for i in range(1,h+1):
    for j in range(1,w+1):
        if i==1 and j==1:
            if s[i][j]=='#':
                dp[i][j]+=1

        elif i==1:
            if s[i][j]=='#' and s[i][j-1]=='.':
                dp[i][j]+=dp[i][j-1]+1
            else:
                dp[i][j]=dp[i][j-1]
        elif j==1:
            if s[i][j]=='#' and s[i-1][j]=='.':
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]=dp[i-1][j]

        elif dp[i-1][j]==dp[i][j-1]:
            if s[i][j]=='#' and s[i-1][j]=='.' and s[i][j-1]=='.':
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]=dp[i-1][j]

        elif dp[i-1][j]<dp[i][j-1]:
            if s[i][j]=='#' and s[i-1][j]=='.':
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]=dp[i-1][j]
        else:
            if s[i][j]=='#' and s[i][j-1]=='.':
                dp[i][j]=dp[i][j-1]+1
            else:
                dp[i][j]=dp[i][j-1]




print(dp[-1][-1])