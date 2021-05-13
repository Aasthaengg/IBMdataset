# B - Time Limit Exceeded
N, T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]

ans = float("inf")

for i in range(N):
	if CT[i][1] <= T:
		ans = min(ans, CT[i][0])
	else:
		pass

if ans == float("inf"):
	ans = "TLE"

print(ans)
