import sys
sys.setrecursionlimit(10**7)

N = int(input())
h = list(map(int, input().split()))

dp = [float("inf")] * N

# # 足場 i から 足場 N - 1 まで移動するときのコストの最小値
# def rec(i):
#     if dp[i] >= 0:
#         return dp[i]
    
#     res = -1
#     if i == N - 1:
#         res = 0
#     elif i == N - 2:
#         res = rec(i + 1) + abs(h[i + 1] - h[i])
#     else:
#         res =  min(rec(i + 1) + abs(h[i + 1] - h[i]), rec(i + 2) + abs(h[i + 2] - h[i]))
    
#     dp[i] = res
#     return dp[i]

# print(rec(0))

dp[N - 1] = 0
for i in reversed(range(N - 1)):
    for j in range(1, 3):
        if (i + j <= N - 1):
            dp[i] = min(dp[i], dp[i + j] + abs(h[i + j] - h[i]))

print(dp[0])