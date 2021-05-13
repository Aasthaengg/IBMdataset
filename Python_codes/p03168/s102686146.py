from sys import stdin, stdout
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	n = int(rl())
	P = [0]
	P.extend(list(rlf()))

	dp = [[0 for j in range(n+1)] for i in range(n+1)]
	dp[0][0] = 1
	for c in range(1, n + 1):
		dp[0][c] = dp[0][c-1]*(1 - P[c])

	for r in range(1, n + 1): 
		for c in range(r, n + 1): 
			dp[r][c] = P[c]*dp[r-1][c-1] + (1- P[c])*dp[r][c-1]

	ans = sum(dp[i][n] for i in range(m.ceil(n/2), n + 1))
	print(ans)
	
	stdout.close()

if __name__ == "__main__":
	main()