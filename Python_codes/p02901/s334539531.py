# coding: utf-8
# Your code here!
#D流用したので文字滅茶苦茶
N,M=map(int,input().split())

dp=[10**10]*2**N
dp[0]=0

for _ in range(M):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    
    can_open=sum([2**(c[i]-1) for i in range(len(c))])
    
    for i in range(len(dp))[::-1]:
        if dp[i]!=10**10 and i|can_open<2**N:
            dp[i|can_open]=min(dp[i]+a,dp[i|can_open])


if dp[-1]==10**10:
    print(-1)
else:
    print(dp[-1])
