from itertools import permutations as P

N = int(input())
V = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N+1)]

l = tuple(P(range(3), 2))

for i in range(N):
	for j in range(6):
		a, b = l[j]

		dp[i+1][b] = max(dp[i+1][b], dp[i][a] + V[i][b])

#print(dp)
print(max(dp[-1]))