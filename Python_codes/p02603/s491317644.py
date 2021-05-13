import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [0]*(N+1)
dp[0] = 1000

for i in range(N):
    for j in range(i+1):
        dp[i+1] = max(dp[i+1], dp[j]%A[j]+dp[j]//A[j]*A[i])

print(max(dp))