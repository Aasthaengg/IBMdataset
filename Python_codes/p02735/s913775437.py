from sys import stdin, stdout
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	H, W = rli()
	M = []
	#0 white, 1 black
	for _ in range(H):
		row = list(rll()[0])
		row = list(map(lambda x: 0 if x == "." else 1, row))
		M.append(row)

	dp = [[INF if i != 0 and j != 0 else 0 for j in range(W)] for i in range(H)]
	dp[0][0] = 1 if M[0][0] == 1 else 0
	
	for c in range(1, W):
		if M[0][c-1] == 0 and M[0][c] == 1:
			dp[0][c] = dp[0][c-1] + 1
		else:
			dp[0][c] = dp[0][c-1]
	for r in range(1, H):
		if M[r-1][0] == 0 and M[r][0] == 1:
			dp[r][0] = dp[r-1][0] + 1
		else:
			dp[r][0] = dp[r-1][0]

	for r in range(1, H):
		for c in range(1, W):
			c1, c2 = INF, INF
			if M[r-1][c] == 0 and M[r][c] == 1:
				c1 = dp[r-1][c] + 1
			if M[r][c-1] == 0 and M[r][c] == 1:
				c2 = dp[r][c-1] + 1
			c1 = dp[r-1][c] if c1 == INF else c1 
			c2 = dp[r][c-1] if c2 == INF else c2
			dp[r][c] = min(c1, c2)
	print(dp[-1][-1])
	stdout.close()

if __name__ == "__main__":
	main()