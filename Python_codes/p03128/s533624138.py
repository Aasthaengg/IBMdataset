
mnum = [0,2,5,5,4,5,6,3,7,6]



N,M = map(int, input().split())

A = list(map(int, input().split()))

dp=[-1 for _ in range(N + 100)]
dp[0] = 0

for i in range(N):
	for m in A:
		need = mnum[m]
		if(dp[i] >= 0):
			dp[i+need] = max(dp[i+need], dp[i] * 10 + m);

print(dp[N])