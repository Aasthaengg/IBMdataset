from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import math

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	n, k = rli()
	A = list(rli())
	dp = [INF for _ in range(n)]
	dp[0] = 0
	for i in range(1, n):
		for j in range(max(0, i-k), i):
			dp[i] = min(dp[i], dp[j] + abs(A[j] - A[i]))
	print(dp[-1])
	stdout.close()

if __name__ == "__main__":
	main()