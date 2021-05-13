import sys
input = sys.stdin.readline

H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
dp = [10**18]*(H+1)
dp[0] = 0

for i in range(H):
    for A, B in AB:
        j = min(H, i+A)
        dp[j] = min(dp[j], dp[i]+B)

print(dp[H])