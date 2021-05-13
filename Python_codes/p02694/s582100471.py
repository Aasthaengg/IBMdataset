import sys
from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))



def solve():
	n = int(input()); x = 100
	y = 0
	while x < n:
		x += (x)//100
		y += 1
	print(y)


	





		

if __name__ == "__main__":
	solve()