from sys import stdin, stdout
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	n, k = rli()
	A = list(rli())
	dp = [0 for _ in range(k + 1)]
	for i in range(1, k + 1):
		for num in A:
			if i - num < 0:
				continue
			if dp[i]: 
				break
			if not dp[i-num]: 
				dp[i] = 1
	print("First" if dp[-1] else "Second")
	stdout.close()

if __name__ == "__main__":
	main()