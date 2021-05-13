import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

A, B = rl()

if (A+B) % 2 == 1:
	print('IMPOSSIBLE')
else:
	print((A+B)//2)
