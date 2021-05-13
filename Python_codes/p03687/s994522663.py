s = input()
n = len(s)

chars = [chr(i) for i in range(97, 97+26)]

res = 1 << 30
for c in chars:
	cnt = 0
	t = s
	while len(set(list(t))) > 1:
		u = []
		for i in range(len(t) - 1):
			if t[i] == c or t[i + 1] == c:
				u.append(c)
			else:
				u.append(t[i])
		cnt += 1
		t = ''.join(u)
	res = min(res, cnt)

print(res)
