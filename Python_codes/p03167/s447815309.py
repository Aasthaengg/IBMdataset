from sys import stdin, stdout
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	MOD = 10**9 + 7
	rows, cols = rli()
	dp = [[0 for __ in range(cols)] for _ in range(rows)]
	A = []
	for _ in range(rows):
		row = []
		for c in rll()[0]:
			if c == "#":
				row.append(1)
			else:
				row.append(0)
		A.append(row)

	dp[0][0] = 1
	for c in range(1, cols):
		if A[0][c] == 1:continue
		dp[0][c] = dp[0][c-1]

	for r in range(1, rows):
		if A[r][0] == 1: continue
		dp[r][0] = dp[r-1][0]

	for r in range(1, rows):
		for c in range(1, cols):
			if A[r][c] == 1: continue
			dp[r][c] = dp[r-1][c] + dp[r][c-1]

	print(dp[-1][-1] % MOD)

	stdout.close()

if __name__ == "__main__":
	main()