N, M = list(map(int, input().split()))
S = list(map(int, input().split()))
T = list(map(int, input().split()))
d = [[0 for i in range(M + 1)] for j in range(N + 1)]
mod = 1000000007

for i in range(1, N+1):
	sum = 0
	for j in range(1, M + 1):
		if S[i - 1] == T[j - 1]:
			sum += d[i - 1][j - 1] + 1
		d[i][j] = (d[i - 1][j] + sum) % mod
print((d[N][M] + 1)%mod)