import math
n,h = map(int ,raw_input().split())
ais = [map(int, raw_input().split()) for _ in range(n)]
ais.sort(key = lambda x: (-x[1],x[0]))
r,m,cumul = h, max(ais)[0],0
r = (h+m-1)/m
for i in range(len(ais)):
	cumul += ais[i][1]
	r = min(r, i + 1 + (max(h - cumul, 0) + m - 1)/ m )
	if h <= cumul:
		break
print r
