import sys
 
sys.setrecursionlimit(1000000)
n, m, *a = map(int, open(0).read().split())
dp = [1] + [-1] * n
dp[1] = 1
for i in a:
    dp[i] = 0
 
def count(n):
    if dp[n] != -1:
        return dp[n]
    dp[n] = (count(n - 1) + count(n - 2)) % (10**9 + 7)
    return dp[n]
 
 
print(count(n))