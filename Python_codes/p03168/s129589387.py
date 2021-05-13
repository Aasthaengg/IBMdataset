from sys import stdin, stdout


def solve():
    n = int(input())
    A = [float(i) for i in stdin.readline().split()]
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(0, i+1):
            if j == 0: dp[i][j] = (1 - A[i-1]) * dp[i-1][j]
            else: dp[i][j] = (A[i-1] * dp[i-1][j-1]) + ((1 - A[i-1]) * dp[i-1][j])
    ans = 0
    for i in range((n+1)//2, n+1):
        ans += dp[-1][i]
    return ans

print(solve())

