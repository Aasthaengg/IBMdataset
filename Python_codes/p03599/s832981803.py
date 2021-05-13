def dense(w, s):
	if s + w == 0:
		return 0
	return s / (w + s) * 100

def resolve():
	A, B, C, D, E, F = map(int, input().split())
	waters = set()
	sugars = set()

	for i in range(31):
		for j in range(31):
			v = A*i*100 + B*j*100
			if v > F:
				continue
			waters.add(v)
	for i in range(3001):
		for j in range(3001):
			v = i*C + j*D
			if v > F:
				continue
			sugars.add(v)
	ans_w, ans_s = 0, 0
	for w in waters:
		for s in sugars:
			if w + s > F or s > w//100*E or s + w == 0:
				continue
			if dense(w, s) >= dense(ans_w, ans_s):
				ans_w, ans_s = w, s
	print(ans_w + ans_s, ans_s)
resolve()