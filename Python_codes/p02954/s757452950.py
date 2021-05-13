import sys, math
from collections import defaultdict
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

S = rs()

r = 0
ans = [0]*len(S)
for i, s in enumerate(S):
	if s == 'L':
		ans[i] += r//2
		ans[i-1] += r-r//2
		r = 0
	else:
		r += 1
l = 0
for i, s in enumerate(S[::-1]):
	if s == 'R':
		ans[~i] += l//2
		ans[~(i-1)] += l-l//2
		l = 0
	else:
		l += 1
print(*ans)
