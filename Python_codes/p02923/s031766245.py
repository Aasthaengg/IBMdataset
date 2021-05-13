N = int(input())
H = list(map(int, input().split()))
dp = [0] * N
res = 0
for i in range(N-2, -1, -1):
    if H[i] >= H[i+1]:
        dp[i] = dp[i+1] + 1
print(max(dp))