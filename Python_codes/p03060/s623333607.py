import sys
# from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)



def solve():
	n = int(inp()); a = read(); b = read()
	ans = 0
	for i in range(n):
		ans += max(0, a[i]-b[i])
	print(ans)

	





		

if __name__ == "__main__":
	solve()