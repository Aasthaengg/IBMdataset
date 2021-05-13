import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

S = rs()
T = rs()

ans = 0
for i in range(3):
	if S[i] == T[i]:
		ans += 1
print(ans)