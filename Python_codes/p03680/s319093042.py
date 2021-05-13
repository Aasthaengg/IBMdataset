ais = [int(raw_input()) for oo in range(int(raw_input()))]
seen = set([])
u = 0
while((u!= 1) and (u not in seen)):
	seen.add(u)
	u = ais[u] - 1

print len(seen) if u == 1 else -1
