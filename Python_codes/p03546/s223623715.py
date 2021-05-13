


h,w = map(int, raw_input().split())
cost = []
for _ in range(10): 
	cost.append(map(int,raw_input().split()))


mat = [map(int, raw_input().split()) for ii in range(h)]

h = {(u,v):cost[u][v] for u in range(10) for v in range(10)}
for t in range(10):
	for u in range(10):
		for v in range(10):
			for w in range(10):
				h[(u,v)] = min(h[(u,v)], h[(u,w)] + h[(w,v)])
cumul = 0
for e in mat:
	for el in e:
		if el != -1:
			cumul += h[(el,1)]
print cumul