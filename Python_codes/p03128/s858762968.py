N, M = map(int, input().split())
A = list(map(int, input().split()))

costs = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# 優先度：桁数, [要素(降順)]
dp = [[0, []] for _ in range(N + 1)]
for a in A:
	cost = costs[a]
	for n in range(N):
		if n != 0 and dp[n][0] == 0:
			continue
		ni = n + cost
		if N < ni:
			break
		np = [dp[n][0] + 1, sorted(dp[n][1] + [a], reverse=True)]
		if dp[ni] < np:
			dp[ni] = np

print(*sorted(dp[N][1], reverse=True), sep="")
