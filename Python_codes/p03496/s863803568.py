
def f(n,ais):
	ma,mi = max(ais), min(ais)
	res = []
	if ma + mi > 0:
		j = [j for j in range(len(ais)) if ais[j] == ma][0]
		for i in range(len(ais)):
			if ais[i] != ma:
				ais[i] += ais[j]
				res.append([j+1,i+1])

		for i in range(1,len(ais)):
			if ais[i-1] > ais[i]:
				ais[i] += ais[i-1]
				res.append([i-1+1, i+1])
	else:
		j = [j for j in range(len(ais)) if ais[j] == mi][0]
		for i in range(len(ais)):
			if ais[i] != mi:
				ais[i] += ais[j]
				res.append([j+1, i+1])
		for i in range(len(ais)-1, 0, -1):
			if not(ais[i - 1] <= ais[i ]):
				ais[i-1] += ais[i]
				res.append([i+1, i-1+1])
	print len(res)
	for u,v in res:
		print u,v
f(int(raw_input()),map(int, raw_input().split()))
