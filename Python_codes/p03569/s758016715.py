import sys

s = input()
s_x = s.replace('x', '')

if len(s) == 1:
	print(0)
	sys.exit()

middle, mod = divmod(len(s_x),2)
middle += mod
if s_x[:middle] != s_x[::-1][:middle]:
	print(-1)
	sys.exit()

x_count = []
cnt = 0
for i in range(len(s)):
	if s[i] != 'x':
		x_count.append(cnt)
		cnt = 0
	else:
		cnt += 1
x_count.append(cnt)

ans = 0
for i in range(len(x_count)):
	ans += abs(x_count[i] - x_count[-(1+i)])

print(ans//2)