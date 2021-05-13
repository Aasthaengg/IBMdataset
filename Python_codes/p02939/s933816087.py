s = list(input())
n = len(s)

p, t = '', ''

cnt = 0

for char in s:
	t += char
	if p == t:
		continue
	cnt += 1
	p, t = t, ''

print(cnt)