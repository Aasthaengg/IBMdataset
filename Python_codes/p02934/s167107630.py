import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N = ri()
A = rl()

m = 1
for a in A:
	m *= a
s = 0
for a in A:
	s += m/a
print(m/s)
