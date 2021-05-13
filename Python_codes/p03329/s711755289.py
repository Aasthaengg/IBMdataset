import sys
sys.setrecursionlimit(10**7)
def f(n):
    if dp[n] != -1:
        return dp[n]
    res = N
    for i in range(N):
        if n < 6**i:
            break
        res = min(res, f(n-6**i)+1)
    for i in range(N):
        if n < 9**i:
            break
        res = min(res, f(n-9**i)+1)
    dp[n] = res
    return res

N = int(input())
dp = [-1]*(N+1)
dp[0] = 0
f(N)
print(dp[N])