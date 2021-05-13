n = int(input())
pl = list(map(float,input().split()))

# dp[i][j] i回目でj回表がでる確率
dp = [[0 for j in range(n+1)] for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] += pl[i] * dp[i][j]
        dp[i+1][j] += (1-pl[i]) * dp[i][j]

def ceil(a, b):
   return a // b + (a % b > 0)
print(sum(dp[-1][ceil(n,2):]))