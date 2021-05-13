# https://betrue12.hateblo.jp/entry/2018/10/06/224032

n = int(input())
x, y, h = [], [], []
for i in range(n):
	a, b, c = map(int, input().split())
	x.append(a)
	y.append(b)
	h.append(c)


for i in range(101):
	for j in range(101):
		H = -1
		Hmax = 2 * 10 ** 9
		success = True
		for k in range(n):
			d = abs(i - x[k]) + abs(j - y[k])
			if h[k] > 0:
				H2 = h[k] + d
				if H > 0 and H != H2:
					success = False
					break
				else:
					H = H2
			else: # h[k] == 0
				Hmax = min(Hmax, d)
		
		if success and H <= Hmax:
			print(i, j, H)
			exit()