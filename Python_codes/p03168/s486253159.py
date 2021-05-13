import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(float, input().split()))

dp = [[0]*3100 for _ in range(3100)]

N = int(input())
P = input_nums()

dp[0][0] = 1.0

for i in range(N):
    for j in range(i+1):
        dp[i+1][j+1] += dp[i][j] * P[i]
        dp[i+1][j] += dp[i][j] * (1-P[i])

res = 0.0
a = ((N+1)//2)
for j in range(a, N+1):
    res += dp[N][j]
print(res)
