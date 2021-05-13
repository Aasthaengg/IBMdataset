import sys
mod=10**9+7
input=sys.stdin.buffer.readline
n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
dp=[ [0 for _ in range(m)] for _ in range(n)]
for i in range(0,n):
    for j in range(0,m):
        ret=0
        if i-1>=0:
            ret+=dp[i-1][j]
        if j-1>=0:
            ret+=dp[i][j-1]
        if i-1>=0 and j-1>=0:
            ret-=dp[i-1][j-1]
        if s[i]==t[j]:
            ret+=1
            if i-1>=0 and j-1>=0:
                ret+=dp[i-1][j-1]
        if ret>=mod:
            ret%=mod
        if ret<0:
            ret+=mod
        dp[i][j]=ret
print((dp[n-1][m-1]+1))

