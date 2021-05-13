N, W = map(int, input().split())
wlist = [0] * N
vlist = [0] * N
for i in range(N):
	wlist[i], vlist[i] = map(int, input().split())
minw = min(wlist)
w = list()
for i in range(4):
	w.append(list())
for i in range(N):
	w[wlist[i] - minw].append(vlist[i])
for i in range(4):
	w[i].sort(reverse = True)
ans = 0
sumw0 = 0
sumv0 = 0
for i in range(len(w[0]) + 1):
	sumw1 = 0
	sumv1 = 0
	for j in range(len(w[1]) + 1):
		sumw2 = 0
		sumv2 = 0
		for k in range(len(w[2]) + 1):
			sumw3 = 0
			sumv3 = 0
			for l in range(len(w[3]) + 1):
				sumw = sumw0 + sumw1 + sumw2 + sumw3
				sumv = sumv0 + sumv1 + sumv2 + sumv3
				if sumw <= W:
					ans = max(ans, sumv)
				if l != len(w[3]):
					sumw3 += minw + 3
					sumv3 += w[3][l]
			if k != len(w[2]):
				sumw2 += minw + 2
				sumv2 += w[2][k]
		if j != len(w[1]):
			sumw1 += minw + 1
			sumv1 += w[1][j]
	if i != len(w[0]):
		sumw0 += minw
		sumv0 += w[0][i]
print(ans)