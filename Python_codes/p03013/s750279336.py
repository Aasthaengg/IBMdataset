import sys
sys.setrecursionlimit(200010)

n, m = map(int, input().split())
a = [int(input()) for i in range(m)]
b = [0]*(n+1)
dp = [-1]*(n+1)
for e in a:
    b[e] = 1
dp[0] = 1


def solve(k):
    if(b[k] == 1):
        return 0
    if(dp[k] != -1):
        return dp[k]
    if(k < 0):
        return 0
    tmp = solve(k-1)+solve(k-2)
    dp[k] = tmp % 1000000007
    return tmp


print(solve(n) % (1000000007))
