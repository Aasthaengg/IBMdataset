import sys
import resource

sys.setrecursionlimit(200000)

n = int(input())
h = list(map(int, input().split()))

dp = []
for i in range(n):
    dp.append(-1)
 
def flog(m):
    if dp[m] != -1:
        return dp[m]
    if m == 0:
        dp[m] = 0
        return 0
    if m == 1:
        dp[m] = abs(h[0]-h[1])
        return dp[m]
    else:
        dp[m] = min(flog(m-1) + abs(h[m-1] - h[m]),flog(m-2) + abs(h[m-2] - h[m]))
        return dp[m]
  
print(flog(n-1))