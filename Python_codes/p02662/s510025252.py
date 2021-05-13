# -*- coding: utf-8 -*-

N,S = list(map(int, input().rstrip().split()))

# Add dummy data at first position
A_list = [None] + list(map(int, input().rstrip().split()))
#-----

mod = 998244353

dp = [ [0]*(S+1) for _ in range(N+1) ]
dp[0][0] = 1

for i in range(N):
    for j in range(S+1):
        if (j - A_list[i+1]) >=0:
            dp[i+1][j] = dp[i][j - A_list[i+1]]
        
        dp[i+1][j] += 2*dp[i][j]
        dp[i+1][j] %= mod

print(dp[N][S])
