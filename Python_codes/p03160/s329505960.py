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
	n = int(rl())
	A = list(rli())
	dp = [INF for _ in range(n)]
	dp[0] = 0
	dp[1] = abs(A[0] - A[1])
	for i in range(2, n):
		dp[i] = min(dp[i], 
					dp[i-2] + abs(A[i-2]-A[i]),
					dp[i-1] + abs(A[i-1]-A[i])
					)
	print(dp[-1])
	stdout.close()

if __name__ == "__main__":
	main()