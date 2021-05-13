import sys
# from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)



def solve():
	a, b, t = read()
	print(int((t+.5)//a)*b)


	





		

if __name__ == "__main__":
	solve()