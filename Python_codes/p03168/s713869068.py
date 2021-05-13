import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n = int(input())
p = list(map(float, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j] * (1-p[i-1]) + dp[i-1][j-1] * p[i-1]
print(sum(dp[n][j] for j in range(n//2+1, n+1)))