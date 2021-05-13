import sys
N = int(sys.stdin.readline().rstrip())
S = list(map(str, sys.stdin.readline().rstrip()))

left = [None] * N
right = [None] * N
tmp_white,tmp_black = 0,0
for i in range(N):
	if S[i] == '#':
		tmp_black += 1
	left[i] = tmp_black

for i in range(N):
	if S[-(i+1)] == '.':
		tmp_white += 1
	right[-(i+1)] = tmp_white

ans = min(left[-1], right[0])

for i in range(1,N):
	ans = min(ans, left[i-1] + right[i])

print(ans)