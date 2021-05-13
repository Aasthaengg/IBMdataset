def resolve():
	n = int(input())
	a = list(map(int, input().split()))
	t = dict()
	for i in a:
		if t.get(i):
			t[i] += 1
		else:
			t[i] = 1
	a, b = 0, 0
	for k in t:
		if t[k] >= 4:
				a = max(a, k)
				b = max(b, k)
		elif t[k] >= 2:
			if k > a:
				b = a
				a = k
	print(a*b)
resolve()