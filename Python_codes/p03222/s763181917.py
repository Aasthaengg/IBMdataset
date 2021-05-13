import sys,queue,math,copy,itertools,bisect,collections,heapq
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

H,W,K = LI()

dp = [[0] * W for _ in range(H+1)]
dp[0][0] = 1

good = []
for ami in range(2**(W-1)):
    b = 1
    m = -2
    for i in range(W-1):
        if b & ami:
            if i <= m + 1:
                break
            m = i
        b <<= 1
    else:
        s = []
        b = 1
        for i in range(W):
            s.append(ami & b > 0)
            b <<= 1
        good.append([0] + s + [0])

for i in range(H):
    for ami in good:
        for j in range(W):
            if ami[j] == 0 and ami[j+1] == 0:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            elif ami[j] == 1:
                dp[i+1][j-1] = (dp[i+1][j-1] + dp[i][j]) % MOD
            else:
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD

print(dp[-1][K-1])