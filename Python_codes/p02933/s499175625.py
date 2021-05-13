import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

a = ri()
s = rs()

if a >= 3200:
	print(s)
else:
	print('red')
