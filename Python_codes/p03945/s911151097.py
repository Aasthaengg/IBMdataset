s = list(input())
s.append('X')
cnt = 0
for n in range(len(s)-1):
	if s[n] != s[n+1]:
		cnt += 1
print(cnt - 1)