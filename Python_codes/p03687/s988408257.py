S = input()
ans = len(S)
for i in range(26):
	c = chr(ord('a') + i)
	t = list(S)
	while not all(a==t[0] for a in t):
		u = []
		for a,b in zip(t,t[1:]):
			if a==c or b==c:
				u.append(c)
			else:
				u.append(a)
		t = u
	tmp = len(S) - len(t)
	ans = min(ans, tmp)
print(ans)