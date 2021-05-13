import math
from decimal import *

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0 for i in range(3)] for i in range(n)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]
for i in range(1, n):
    for j in range(3):
        for x in range(3):
            if(x!= j):
                dp[i][j] = max(arr[i][j]+ dp[i-1][x], dp[i][j])
ans = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(ans)