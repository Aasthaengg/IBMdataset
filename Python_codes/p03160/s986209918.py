inf = 10**9
n = int(input())
h = [int(i) for i in input().split()]
dp = [inf for i in range(n+10)]

def chmin(a,b):
    if (a>b):
        return b
    else:
        return a
      
dp[0] = 0
for i in range(1,n):
    dp[i] = chmin(dp[i],dp[i-1]+abs(h[i]-h[i-1]))
    if i>1:
      dp[i] = chmin(dp[i],dp[i-2]+abs(h[i]-h[i-2]))
print(dp[n-1])