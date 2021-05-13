def dense(a, b):
	return b / (a+b)

def resolve():
	a, b, c, d, e, f = map(int, input().split())
	ws = set()
	ss = set()
	for i in range(31):
		for j in range(31):
			if a*100*i + b*100*j <= f:
				ws.add(a*100*i + b*100*j)
	for i in range(3001):
		for j in range(3001):
			if c*i + j*d <= f:
				ss.add(c*i + j*d)
	ans_w, ans_s = -1, 0
	lim = e / (100+e)
	for wv in ws:
		for sv in ss:
			if wv + sv > f:
				continue
			if wv + sv == 0:
				continue
			if lim >= dense(wv, sv):
				if dense(ans_w, ans_s) <= dense(wv, sv):
					ans_w, ans_s = wv, sv
	print(ans_w + ans_s, ans_s)
resolve()