#!/usr/bin/env python3

# from pprint import pprint

def recur(parr, curp, curi, heads):
    # if dp[curi][heads] != -1:
    # return dp[curi][heads]
    if curi >= len(parr):
        if heads >= len(parr)//2 + 1:
            return curp
        else:
            return 0

    return (recur(parr, curp*parr[curi], curi+1, heads+1)
            + recur(parr, curp*(1-parr[curi]), curi+1, heads))

n = int(input())

parr = [float(i) for i in input().split(' ')]

# print(recur(parr, 1, 0, 0))

dp = [[0]*(n+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(i, -1, -1):
        # heads
        heads = dp[i-1][j-1] if j > 0 else 0
        # tails
        tails = dp[i-1][j]
        dp[i][j] = heads*parr[i-1] + tails*(1-parr[i-1])

print(sum(dp[n][n//2+1:]))
