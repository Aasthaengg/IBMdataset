import sys
import math
from  collections import defaultdict


# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

mod = 1000000007

def solve(test):
	h, w = map(int, input().split())
	grid = []
	for i in range(h):
		grid.append(list(input()))


	dp = [[0 for j in range(w)] for i in range(h)]
	dp[0][0] = 1
	for j in range(1, w):
		if grid[0][j] == '.':
			dp[0][j] += dp[0][j - 1]

	for i in range(1, h):
		if grid[i][0] == '.':
			dp[i][0] += dp[i - 1][0]

	for i in range(1, h):
		for j in range(1, w):
			if grid[i][j] == '.':
				dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % mod

	ans = dp[-1][-1]
	print(ans)




if __name__ == "__main__":
	test_cases = 1
	for t in range(1, test_cases + 1):
		solve(t)
