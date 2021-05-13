import sys
def input():
	return sys.stdin.readline()[:-1]
d = int(input())
c = list(map(int, input().split()))
C = sum(c)
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

def score(t):
	res = 0
	minus = 0
	last = [0 for _ in range(26)]
	for i, x in enumerate(t):
		minus += C - c[x-1] * (i - last[x-1] + 1)
		res -= minus
		res += s[i][x-1]
		last[x-1] = i+1
		print(res)
	return

score(t)