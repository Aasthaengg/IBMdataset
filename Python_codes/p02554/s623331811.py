# from functools import lru_cache

n = int(input())


# @lru_cache(maxsize=None)
# def dp(num, typ, mod=10 ** 9 + 7):
#     print(num, typ)
#     if num == 1:
#         if typ == 1:  # contain 0 not 9
#             return 1
#         elif typ == 2:  # contain 9 not 0
#             return 1
#         elif typ == 3:  # not contain
#             return 8
#         elif typ == 0:
#             return 0

#     if typ == 0:
#         return (dp(num - 1, 1) + dp(num - 1, 2) + dp(num - 1, 0) * 10) % mod
#     elif typ == 1:  # contain 0 not 9
#         return (dp(num - 1, 1) * 9 + dp(num - 1, 3)) % mod
#     elif typ == 2:  # contain 9 not 0
#         return (dp(num - 1, 2) * 9 + dp(num - 1, 3)) % mod
#     elif typ == 3:  # not contain
#         return (dp(num - 1, 3) * 8) % mod


# print(dp(n, 0))

dp = [[0 for j in range(4)] for i in range(n + 1)]

mod = 10 ** 9 + 7
for i in range(1, n + 1):
    for j in range(4):
        if j == 0:
            dp[i][j] = (dp[i - 1][0] * 10 + dp[i - 1][1] + dp[i - 1][2]) % mod
            if i == 1:
                dp[i][j] = 0
        elif j == 1:
            dp[i][j] = (dp[i - 1][1] * 9 + dp[i - 1][3]) % mod
            if i == 1:
                dp[i][j] = 1
        elif j == 2:
            dp[i][j] = (dp[i - 1][2] * 9 + dp[i - 1][3]) % mod
            if i == 1:
                dp[i][j] = 1
        elif j == 3:
            dp[i][j] = (dp[i - 1][3] * 8) % mod
            if i == 1:
                dp[i][j] = 8

print(dp[n][0])

