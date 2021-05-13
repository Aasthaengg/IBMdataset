N, A, B = map(int, input().split())
X = list(map(int, input().split()))

# x -----> x ----> x            y ----> y                z ----> z

# テレポートとテレポートの間を１グループとすると、各グループは独立している
# 行った道を引き返すことはない。基本的に左から右への移動で十分。

dp = [-1] * (N + 1)
dp[0], dp[1] = 0, 0

for i in range(1, N):
    dp[i + 1] = min(dp[i] + A * (X[i] - X[i - 1]), dp[i] + B)

# print('dp', dp)
print(dp[-1])
