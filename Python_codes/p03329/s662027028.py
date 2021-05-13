import sys
def I(): return int(sys.stdin.readline().rstrip())
N = I()
dp = [float('INF')]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    dp[i] = dp[i-1]+1
    num6,num9 = 6,9
    while i-num6>=0:
        dp[i] = min(dp[i],dp[i-num6]+1)
        num6 *= 6
    while i-num9>=0:
        dp[i] = min(dp[i],dp[i-num9]+1)
        num9 *= 9
print(dp[-1])
