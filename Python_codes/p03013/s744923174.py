import sys

mod = 1000000007

N, M = map(int, sys.stdin.readline().split())
A = set()
for _ in range(M):
    a = int(sys.stdin.readline())
    A.add(a)

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 0 if 1 in A else 1
for i in range(1, N):
    if i+1 in A:
        continue
    dp[i+1] = dp[i] + dp[i-1]
    dp[i+1] %= mod

# print(dp)
print(dp[N])