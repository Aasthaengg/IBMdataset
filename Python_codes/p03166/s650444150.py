from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict
import math as m

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

setrecursionlimit(10000)

def main():
	n, m = rli()
	G = [[] for i in range(n+1)]
	for _ in range(m):
		u, v = rli()
		G[u].append(v)
	ans = 0
	memo = [-1 for _ in range(n+1)]

	def longest(v):
		if memo[v] > -1:
			return memo[v]
		pathlen = 0
		for nbhr in G[v]:
			pathlen = max(pathlen, 1 + longest(nbhr))
		memo[v] = pathlen
		return pathlen

	for i in range(1, n+1):
		ans = max(ans, longest(i))

	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()