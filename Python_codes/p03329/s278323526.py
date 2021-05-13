import sys
sys.setrecursionlimit(10**9)
n = int(input())
pow6s = [6, 36, 216, 1296, 7776, 46656]
pow9s = [9, 81, 729, 6561, 59049]
dp = [-1] * (n+1)
def dfs(n):
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    mincount = n + 1
    for p6 in pow6s:
        if n-p6 >= 0:
            mincount = min(mincount, dfs(n-p6) + 1)
    for p9 in pow9s:
        if n-p9 >= 0:
            mincount = min(mincount, dfs(n-p9) + 1)
    
    dp[n] = min(mincount, dfs(n-1) + 1)
    return dp[n]

print(dfs(n))
