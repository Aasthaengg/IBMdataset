# We Like AGC

N = int(input())
MOD = 1e+9+7
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for c1 in range(4):
	for c2 in range(4):
		for c3 in range(4):
			dp[3][c1][c2][c3] = 1

dp[3][0][1][2] = 0
dp[3][0][2][1] = 0
dp[3][1][0][2] = 0

for n in range(4, N+1):
	for c1 in range(4):
		for c2 in range(4):
			for c3 in range(4):
				for a in range(4):
				
					if a==2 and c2 == 0 and c3 == 1:
						continue
					if a==2 and c2 == 1 and c3 == 0:
						continue
					if a==2 and c1 == 0 and c3 == 1:
						continue
					if a==2 and c1 == 0 and c2 == 1:
						continue
					if a==1 and c2 == 0 and c3 == 2:
						continue
				
					dp[n][c2][c3][a] += dp[n-1][c1][c2][c3]
					dp[n][c2][c3][a]  = int(dp[n][c2][c3][a]%MOD)
cnt = 0
mod = 1e+9+7
for c1 in range(4):
	for c2 in range(4):
		for c3 in range(4):
			cnt += dp[N][c1][c2][c3]
cnt = int(cnt%mod)
print(cnt)