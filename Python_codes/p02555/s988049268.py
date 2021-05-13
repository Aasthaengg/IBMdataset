from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
import math

setrecursionlimit(10**6)
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')
MOD = 10**9 + 7

def main():
	s = int(rl())

	@lru_cache(None)
	def dp(currsum):
		if currsum == s: return 1
		cnt = 0
		for d in range(3, 2001):
			if currsum + d <= s:
				cnt += dp(currsum + d)
				cnt %= MOD 
		return cnt
	print(dp(0))
	stdout.close()

if __name__ == "__main__":
	main()