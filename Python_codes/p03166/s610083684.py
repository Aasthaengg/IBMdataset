import sys

sys.setrecursionlimit(20000)

n, m = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    lst[x].append(y)

def rec_dp(x):
    global dp
    if dp[x] != -1:
        return dp[x]
    else:
        ans = 0
        for y in lst[x]:
            ans = max(ans, rec_dp(y) + 1)
        dp[x] = ans
        return dp[x]
      
dp = [-1] * n
ans = 0
for _ in range(n):
    ans = max(ans, rec_dp(_))
print(ans)
