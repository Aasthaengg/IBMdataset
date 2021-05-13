s = input()
k = int(input())
cnt = 0
if len(set(list(s))) == 1:
	cnt = k * len(s) // 2
	print(cnt)
	exit()

x, y = 0, 0
t = s + s
for i in range(len(s) - 1):
	if s[i] == s[i + 1]:
		x += 1
		s = s[:i+1] + '#' + s[i+2:]

for i in range(len(t) - 1):
	if t[i] == t[i + 1]:
		y += 1
		t = t[:i+1] + '#' + t[i+2:]

cnt = x + (k - 1) * (y - x)
print(cnt)