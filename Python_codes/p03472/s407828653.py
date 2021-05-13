import math
n,h = map(int ,raw_input().split())
ais = [map(int, raw_input().split()) for _ in range(n)]
ais.sort(key = lambda x: (-x[1],x[0]))
r,m,cumul = h, max(ais)[0],0
for i in range(-1,len(ais)):
	if i >= 0: cumul += ais[i][1]
	r = min(r, i+1 + int(math.ceil(max(0,h - cumul) /  float(m))))
print r
