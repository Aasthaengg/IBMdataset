import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = list(map(int, list(input())))
length = len(N)
# 丁度払うか釣りをもらうか
dp = [[10**18]*2 for _ in range(length+1)]
dp[0][0] = 0
for i in range(1, length+1):
    n = N[-i]
    dp[i][1] = min(dp[i-1][1]+(9-n), dp[i-1][0]+(10-n))
    dp[i][0] = min(dp[i-1][0]+n, dp[i-1][1]+n+1)
    if i==length:
        dp[i][1] = dp[i][1]+1
print(min(dp[-1]))