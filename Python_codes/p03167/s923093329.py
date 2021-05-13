#import
#import math
#import numpy as np
#= int(input())
#= input()
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= {i:[] for i in range(N)}

def mod(num):
    return num % (10 ** 9 + 7)

H, W = map(int, input().split())
dp = [[0] * W for _ in range(H)]

for i in range(H):
    a = input()
    for j in range(W):
        if a[j] == "#":
            dp[i][j] = -1

dp[0][0] = 1
for row in range(H):
    for col in range(W):
        if row != 0 or col != 0:
            if row == 0:
                if dp[row][col] != -1:
                    dp[row][col] = dp[row][col - 1]
                else:
                    dp[row][col] = 0
            elif col == 0:
                if dp[row][col] != -1:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = 0
            else:
                if dp[row][col] != -1:
                    dp[row][col] = mod(dp[row - 1][col] + dp[row][col - 1])
                else:
                    dp[row][col] = 0

print(dp[-1][-1])