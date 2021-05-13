# -*- coding: utf-8 -*-
# D - Digits Parade
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
S = readline().decode().rstrip()
N = len(S)

dp = [0]*13
dp[0] = 1
# if S[0] == '?':
#     rem = pow(10,N,13)
#     for j in range(10):
#         t = rem*j%13
#         dp[t] += 1
# else:
#     s = int(S[0])
#     rem = pow(10,N,13)*s%13
#     dp[rem] += 1

for i in range(N):
    s = S[i]
    ndp = [0]*13
    rem = pow(10,N-i-1,13)
    if s == '?':
        for j in range(10):
            t = rem*j%13
            for k in range(13):
                ndp[(k+t)%13] += dp[k]
                ndp[(k+t)%13] %= MOD
    else:
        s = int(s)
        t = rem*s%13
        for k in range(13):
            ndp[(k+t)%13] += dp[k]
            ndp[(k+t)%13] %= MOD
    dp = ndp
print(dp[5]%MOD)