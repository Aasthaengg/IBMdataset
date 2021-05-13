import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

S = rs()

L = len(S)

dp = [[0] * 13 for i in range(L+1)]

R = [0]*L
d = 1
for i in range(L):
	d %= 13
	R[i] = d
	d *= 10
R.reverse()

dp[0][0] = 1

for i in range(L):
	for j in range(13):
		if S[i] == '?':
			for k in range(10):
				r = (k * R[i] + j) % 13
				dp[i+1][r] = (dp[i+1][r] + dp[i][j]) % mod
		else:
			r = (int(S[i]) * R[i] + j) % 13
			dp[i+1][r] = (dp[i+1][r] + dp[i][j]) % mod
print(dp[L][5])
