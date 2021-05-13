H,W = map(int, input().split())
a = []
for _ in range(H):
	a.append(input())

dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0]=1

for i in range(1,H):
	if a[i][0]=='#':
		dp[i][0] = 0
	else:
		dp[i][0] = dp[i-1][0]

for j in range(1,W):
	if a[0][j]=='#':
		dp[0][j] = 0
	else:
		dp[0][j] = dp[0][j-1]

for i in range(1,H):
	for j in range(1,W):
		if a[i][j]=='#':
			dp[i][j] = 0
		else:
			dp[i][j] = dp[i-1][j]+dp[i][j-1]
ans =dp[H-1][W-1]
ans = ans%((10**9)+7)
print(ans)