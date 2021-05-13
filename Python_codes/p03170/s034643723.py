import sys
import math
from  collections import defaultdict

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def solve(test):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))


	dp = [None for i in range(k + 1)]
	dp[0] = False
	for j in range(1, k + 1):
		dp[j] = False
		for i in range(n):
			if j >= a[i]:
				dp[j] = not dp[j - a[i]]
				if dp[j]:
					break

	print('First' if dp[k] else 'Second')

if __name__ == "__main__":
	test_cases = 1
	for t in range(1, test_cases + 1):
		solve(t)
