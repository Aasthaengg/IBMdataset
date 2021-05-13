## coding: UTF-8
#DP
N = int(input())
U = list(map(int,input().split()))
D = list(map(int,input().split()))

#dp = [[0] * 2] * N #これだとアドレスごとコピーされている
dp = []
for i in range(N):
    dp.append([0] * 2)
dp[0][0] = U[0]
dp[0][1] = U[0] + D[0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + U[i]
    dp[i][1] = max(dp[i-1][1], dp[i][0]) + D[i]
    #print(dp)
print(dp[N-1][1])