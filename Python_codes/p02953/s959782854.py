import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

N = ri()
H = rl()

last = H.pop()
while H:
	h = H.pop()
	if h > last+1:
		print('No')
		exit()
	elif h > last:
		h -= 1
	last = h
print('Yes')
