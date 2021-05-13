import sys
sys.setrecursionlimit(10**6)
N = int(input())
dp = [-1] * (N + 1)

def rec(n):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    res = n
    i = 0
    while n >= 6 ** i:
        pow6 = 6 ** i
        res = min(res, rec(n - pow6) + 1)
        i += 1
    j = 0
    while n >= 9 ** j:
        pow9 = 9 ** j
        res = min(res, rec(n - pow9) + 1)
        j += 1
    dp[n] = res
    return res
print(rec(N))