s = list(input())

S = set(s)
res = 0
for k in S:
	t = s[::]
	while len(set(t)) != 1:
		t.pop()
		for i in range(len(t) - 1):
			if t[i] == k or t[i + 1] == k:
				t[i] = k
			else:
				t[i] = t[i]
	ma = len(t)
	res = max(res, len(t))

print(len(s) - res)