mod = 1000000007
from sys import setrecursionlimit

setrecursionlimit(100000)


def valid(i, j, n, m):
	if 0 <= i < n and 0 <= j < m and good[i][j]:
		return True
	return False


def solve(i, j):
	if dp[i][j] != -1:
		return dp[i][j]
	if i == n - 1 and j == m - 1:
		return 1
	sm = 0
	if valid(i + 1, j, n, m):
		sm += solve(i + 1, j)
	if valid(i, j + 1, n, m):
		sm += solve(i, j + 1)
	dp[i][j] = sm % mod
	return dp[i][j]


n, m = map(int, input().split())
good = [[] for i in range(n)]
for i in range(n):
	s = input()
	for j in range(m):
		if s[j] == '.':
			good[i].append(True)
		else:
			good[i].append(False)

dp = [[-1 for i in range(m)] for j in range(n)]
print(solve(0, 0))
