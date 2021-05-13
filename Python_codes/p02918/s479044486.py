n, k = map(int, input().split())
s = input()

cnt = 0
blue = 0
red = 0

for i in range(1, n):
	if s[i] == s[i-1]:
		cnt += 1
	elif s[i-1:i+1] == 'LR':
		blue += 1
	elif s[i-1:i+1] == 'RL':
		red += 1

if k <= min(blue, red):
	cnt += 2 * k
else:
	cnt += 2 * min(blue, red)
	if s[0] == 'R' and s[-1] == 'L':
		cnt += 1
	elif s[0] == 'L' and s[-1] == 'R':
		cnt += 1
	else:
		pass

print(cnt)
