import sys
sys.setrecursionlimit(10 ** 6)

S = input()
N = len(S)
dp = [-1 for i in range(N)]


def f(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    if dp[n] != -1:
        return dp[n]
    elif n - 1 >= 0 and S[n] == S[n - 1]:
        dp[n] = f(n - 2) + 1
        if n - 2 >= 0:
            dp[n] = max(dp[n], f(n - 3) + 2)
        return dp[n]
    else:
        dp[n] = f(n - 1) + 1
        return dp[n]


print(f(N - 1))