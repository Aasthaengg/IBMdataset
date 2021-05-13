import math

def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

N = int(input())

dp = makelist(10, 10)
for n in range(1, N+1):
    s = str(n)
    dp[int(s[-1])][int(s[0])] += 1

ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        ans += dp[a][b] * dp[b][a]

print(ans)
