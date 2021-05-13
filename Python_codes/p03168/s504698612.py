#https://atcoder.jp/contests/dp/tasks/dp_i
import math
N = int(input())
P_List = list(map(float,input().split()))
dp = [[0 for j in range(N + 1)] for i in range(N+1)]
std = math.ceil(N/2)
for i in range(N+1):
    if i == 0:
        dp[i][0] = 1
    else:
        Current_P = P_List[i - 1]
        for j in range(i + 1):
            if (N - i + j) < std:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = dp[i - 1][j]*(1 - Current_P)
            elif j != i:
                dp[i][j] = (dp[i - 1][j]*(1 - Current_P)) + (dp[i - 1][j - 1]*Current_P)
            else:
                dp[i][j] = dp[i - 1][j - 1]*Current_P
    
print(sum(dp[N][math.ceil(std):]))