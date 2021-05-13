import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N = ri()
S = rs()

dp = [[0] * (N+1) for _ in range(N+1)]

ans = 0
for i in range(N):
	for j in range(i+1,N):
		if S[i] == S[j]:
			if i+1 < j+1-(dp[i][j]+1)+1:
				dp[i+1][j+1] = dp[i][j]+1
			else:
				dp[i+1][j+1] = 0
			ans = max(ans, dp[i+1][j+1])
print(ans)