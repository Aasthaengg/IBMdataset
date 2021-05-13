import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

h,w = map(int,readline().split())
maze = []
for _ in range(h):
	maze.append(readline().rstrip().decode('utf-8'))

dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
	for j in range(w):
		if maze[i][j] == "#":
			continue
		if i > 0:
			dp[i][j] += dp[i-1][j]
		if j > 0:
			dp[i][j] += dp[i][j-1]
		dp[i][j]%=10**9+7

print(dp[-1][-1])